from pathlib import Path
import shutil

from black_mamba.testlib import contract, eth_tester
from black_mamba.testlib.test_with_contracts import TestWithContracts


class TestTest(TestWithContracts):

    def test_get_contract_object(self):
        shutil.copy(self.json_compiled_fixture, self.json_compiled_file)
        hello_world_contract = contract("HelloWorld", contract_directory=Path("/tmp"))
        assert hello_world_contract.functions.greet().call() == b"Hello World"

    def test_eth_tester_fixture(self, eth_tester):
        accounts = eth_tester.get_accounts()
        assert len(accounts) == 10
        assert eth_tester.get_balance(accounts[0]) == 1000000000000000000000000

    def test_get_contract_with_parameters_object(self):
        shutil.copy(self.json2_compiled_fixture, self.json2_compiled_file)
        hello_parameters_contract = contract("HelloParameters", [b"Hello Parameters", 45], contract_directory=Path("/tmp"))
        assert hello_parameters_contract.functions.greet().call() == b"Hello Parameters"
        assert hello_parameters_contract.functions.get_index().call() == 45
