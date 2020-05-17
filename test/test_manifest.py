from shutil import copy

from black_mamba.testlib.test_with_contracts import TestWithContracts
from black_mamba.epm.manifest import (ask_meta_from_user,
                                      create_contract_types,
                                      ask_package_version_from_user,
                                      create_sources)


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
        result = ask_meta_from_user()
        assert result == expected_result

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

    def test_ask_package_version_from_user(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "vyper")
        expected_result = ("vyper", "vyper")
        result = ask_package_version_from_user()
        assert result == ("vyper", "vyper")

    def test_create_sources(self):
        if not self.contracts_dir.exists():
            self.contracts_dir.mkdir()
        copy(self.fixtures_dir / "HelloWorld.vy", self.contracts_dir / "HelloWorld.vy")

        results = create_sources("hello", self.contracts_dir)
        result = results["./hello/HelloWorld.vy"]
        assert ('self.greeting = "Hello World"' in result) == True
