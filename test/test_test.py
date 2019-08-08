from pathlib import Path
import shutil

from testlib import contract
from testlib.test_with_contracts import TestWithContracts


class TestTest(TestWithContracts):

    def test_get_contract_object(self):
        shutil.copy(self.json_compiled_fixture, self.json_compiled_file)
        hello_world_contract = contract("HelloWorld", Path("/tmp"))
        assert hello_world_contract.functions.greet().call() == b"Hello World"
