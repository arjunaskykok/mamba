from shutil import copy

from black_mamba.testlib.test_with_contracts import TestWithContracts
from black_mamba.epm.manifest import ask_meta_from_user, create_contract_types


class TestAuth(TestWithContracts):

    def test_ask_meta_from_user(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "vyper")
        expected_result = {
            "authors": ["vyper"],
            "description": "vyper",
            "keywords": ["vyper"],
            "license": "vyper",
            "links": {
                "documentation": "vyper",
                "repo": "vyper",
                "website": "vyper"
            }
        }
        results = ask_meta_from_user()
        assert results == expected_result

    def test_create_contract_types(self):
        if not self.build_contracts_dir.exists():
            self.build_contracts_dir.mkdir()
        copy(self.fixtures_dir / "HelloWorld.json", self.build_contracts_dir / "HelloWorld.json")
        results = create_contract_types(self.build_contracts_dir)
        result = results["HelloWorld"]
        assert result["natspec"]["details"] == "Greetings must be done in a polite way"
        assert result["compiler"]["name"] == "vyper"
        assert "runtime_bytecode" in result.keys()
        assert "deployment_bytecode" in result.keys()
