from json import load
from pathlib import Path
from sys import path
from os import getcwd

import pytest
from web3 import (
    EthereumTesterProvider,
    Web3,
)


esp = EthereumTesterProvider()


@pytest.fixture
def eth_tester():
    return esp.ethereum_tester

@pytest.fixture
def w3():
    return get_w3()

def contract(smart_contract_name, parameters=[], contract_directory=Path('.')):
    build_contracts_dir = contract_directory / Path('build') / Path('contracts')
    contract_json_file = (build_contracts_dir / smart_contract_name).with_suffix('.json')

    with open(contract_json_file, 'r') as smart_contract_build_file:
        json_object = load(smart_contract_build_file)
        if json_object["compiler"]["name"] == "solidity":
            bytecode = json_object["bin"]
        else:
            bytecode = json_object["bytecode"]
        abi = json_object["abi"]
        w3 = get_w3()
        contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor(*parameters).transact({"from": w3.eth.accounts[0]})
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        contract = w3.eth.contract(abi=abi, address=tx_receipt.contractAddress)
        return contract

def get_w3():
    settings_directory = getcwd()
    path.append(settings_directory)
    import settings
    try:
        ganache_cli = settings.ganache_cli
        address = ganache_cli["development"]["address"]
        w3 = Web3(Web3.HTTPProvider(address))
        if w3.isConnected():
            return w3
        else:
            esp = EthereumTesterProvider()
            return Web3(esp)
    except AttributeError:
        return Web3(esp)


class TestContract:

    def setup_method(self, method):
        w3 = get_w3()
        try:
            w3.provider.ethereum_tester
        except AttributeError:
            w3.testing.snapshot()

    def teardown_method(self, method):
        w3 = get_w3()
        try:
            w3.provider.ethereum_tester
        except AttributeError:
            w3.testing.revert(1)
