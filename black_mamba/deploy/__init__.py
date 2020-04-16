from json import load, dump, JSONEncoder
from pathlib import Path
from sys import path
from typing import List, Dict, Optional, Any
from os import PathLike, getcwd, environ

from web3 import Web3
from hexbytes import HexBytes
from web3.datastructures import AttributeDict


class HexJsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        if isinstance(obj, AttributeDict):
            return dict(obj)
        return super().default(obj)

class DeployContract:

    def __init__(self, settings_directory : Path = getcwd()):
        path.append(settings_directory)
        import settings
        networks = settings.networks

        development_network = networks["development"]
        if development_network["mode"]=="HTTP":
            server = "http://" + development_network["host"] + ":" + str(development_network["port"])
            self.w3 = Web3(Web3.HTTPProvider(server))
        elif development_network["mode"]=="IPC":
            ipc_url = development_network["url"]
            self.w3 = Web3(Web3.IPCProvider(ipc_url))
        elif development_network["mode"]=="Websocket":
            server = "ws://" + development_network["host"] + ":" + str(development_network["port"])
            self.w3 = Web3(Web3.WebsocketProvider(server))
        elif development_network["mode"]=="Infura":
            environ["WEB3_INFURA_PROJECT_ID"] = str(development_network["project_id"])
            environ["WEB3_INFURA_API_SECRET"] = str(development_network["api_secret"])
            environ["WEB3_INFURA_SCHEME"] = str(development_network["scheme"])
            if development_network["endpoints"] == "mainnet":
                from web3.auto.infura.mainnet import w3
            elif development_network["endpoints"] == "ropsten":
                from web3.auto.infura.ropsten import w3
            elif development_network["endpoints"] == "goerli":
                from web3.auto.infura.goerli import w3
            elif development_network["endpoints"] == "rinkeby":
                from web3.auto.infura.rinkeby import w3
            elif development_network["endpoints"] == "kovan":
                from web3.auto.infura.kovan import w3
            self.w3 = w3

    def contract(self,
                 smart_contract_name : str,
                 build_contracts_directory : Path = Path(getcwd()) / Path("build") / Path("contracts")):
        contract_json_file = (build_contracts_directory / smart_contract_name).with_suffix('.json')

        with open(contract_json_file, "r") as smart_contract_build_file:
            json_object = load(smart_contract_build_file)
            bytecode = json_object["bytecode"]
            abi = json_object["abi"]
            smart_contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
            return smart_contract

    def deployed_contract(self,
                          smart_contract_name : str,
                          build_contracts_directory : Path = Path(getcwd()) / Path("build") / Path("contracts"),
                          deployed_contracts_directory : Path = Path(getcwd()) / Path("deployed")):
        prefix_deployed_file = "receipt_"
        contract_json_file = (build_contracts_directory / smart_contract_name).with_suffix(".json")
        deployed_name = prefix_deployed_file + smart_contract_name
        deployed_json_file = (deployed_contracts_directory / deployed_name).with_suffix(".json")

        with open(contract_json_file, "r") as smart_contract_build_file, open(deployed_json_file, "r") as smart_contract_deployed_file:
            json_object = load(smart_contract_build_file)
            abi = json_object["abi"]
            deployed_json_object = load(smart_contract_deployed_file)
            address = deployed_json_object["contractAddress"]
            smart_contract = self.w3.eth.contract(abi=abi, address=address)
            return smart_contract

    def deploy_contract(self,
                        smart_contract_name : str,
                        parameters : List = [],
                        transaction_parameters : Dict[str, Optional[Any]] = {},
                        private_key : Optional[str] = None,
                        build_contracts_directory : Path = Path(".") / Path("build") / Path("contracts"),
                        deployed_directory : Path = Path(".") / Path("deployed")):

        smart_contract = self.contract(smart_contract_name, build_contracts_directory)
        smart_contract_constructor = smart_contract.constructor(*parameters)
        if private_key:
            from_account = transaction_parameters["from"]
            nonce = self.w3.eth.getTransactionCount(from_account)
            transaction_parameters["nonce"] = nonce
            tx_built = smart_contract_constructor.buildTransaction(transaction_parameters)
            tx_signed = self.w3.eth.account.signTransaction(tx_built, private_key=private_key)
            tx_hash = self.w3.eth.sendRawTransaction(tx_signed.rawTransaction)
        else:
            if transaction_parameters and not transaction_parameters.get("from", None):
                transaction_parameters["from"] = self.w3.geth.personal.listAccounts()[0]
            if transaction_parameters and not transaction_parameters.get("nonce", None):
                from_account = transaction_parameters["from"]
                nonce = self.w3.eth.getTransactionCount(from_account)
                transaction_parameters["nonce"] = nonce
            tx_hash = smart_contract_constructor.transact(transaction_parameters)
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        tx_dict = dict(tx_receipt)

        receipt_name = "receipt_%s" % smart_contract_name
        receipt_json_file = (deployed_directory / receipt_name).with_suffix('.json')

        with open(receipt_json_file, "w") as json_write_file:
            dump(tx_dict, json_write_file, cls=HexJsonEncoder, indent=4)
