from json import load
from pathlib import Path

import pytest
from web3 import (
    EthereumTesterProvider,
    Web3,
)


@pytest.fixture
def eth_tester():
    return EthereumTesterProvider().ethereum_tester

def contract(smart_contract_name, parameters=[], contract_directory=Path('.')):
    build_contracts_dir = contract_directory / Path('build') / Path('contracts')
    contract_json_file = (build_contracts_dir / smart_contract_name).with_suffix('.json')

    with open(contract_json_file, 'r') as smart_contract_build_file:
        json_object = load(smart_contract_build_file)
        bytecode = json_object["bytecode"]
        abi = json_object["abi"]
        w3 = Web3(EthereumTesterProvider())
        contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor(*parameters).transact()
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        contract = w3.eth.contract(abi=abi, address=tx_receipt.contractAddress)
        return contract
