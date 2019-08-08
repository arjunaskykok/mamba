from pathlib import Path
import shutil

from testlib import contract, eth_tester
from testlib.test_with_contracts import TestWithContracts


class TestTest(TestWithContracts):

    def test_get_contract_object(self):
        shutil.copy(self.json_compiled_fixture, self.json_compiled_file)
        hello_world_contract = contract("HelloWorld", Path("/tmp"))
        assert hello_world_contract.functions.greet().call() == b"Hello World"

    def test_eth_tester_fixture(self, eth_tester):
        shutil.copy(self.json_compiled_fixture, self.json_compiled_file)
        accounts = eth_tester.get_accounts()
        assert len(accounts) == 10
        assert eth_tester.get_balance(accounts[0]) == 1000000000000000000000000
