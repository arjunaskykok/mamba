from shutil import copy
from json import loads

from black_mamba.testlib.test_with_contracts import TestWithContracts
from black_mamba.epm.manifest import (ask_meta_from_user,
                                      create_contract_types,
                                      ask_package_version_from_user,
                                      create_sources,
                                      create_manifest,
                                      write_manifest)


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
        self._copy_helloworld_json()

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
        self._copy_helloworld_vy()

        results = create_sources("hello", self.contracts_dir)
        result = results["./hello/HelloWorld.vy"]
        assert ('self.greeting = "Hello World"' in result) == True

    def test_create_manifest(self):
        contract_types = {
            "HelloWorld": {
                "compiler": {"name": "vyper"}
            }
        }
        meta = {
            "authors": ["Arjuna <arjuna@mamba.blaack>"],
            "license": "GPL"
        }
        package_name = "hello"
        sources = {
            "./hello/HelloWorld.vy": "def greet"
        }
        version = "1.0.0"
        result = create_manifest(contract_types, meta, package_name, sources, version)

        expected_result = {
            'contract_types': {'HelloWorld': {'compiler': {'name': 'vyper'}}},
            'manifest_version': '2',
            'meta': {'authors': ['Arjuna <arjuna@mamba.blaack>'], 'license': 'GPL'},
            'package_name': 'hello',
            'sources': {'./hello/HelloWorld.vy': 'def greet'},
            'version': '1.0.0'
        }
        assert result == expected_result

    def test_write_manifest(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda x: "vyper")
        self._copy_helloworld_json()
        self._copy_helloworld_vy()
        write_manifest(self.build_contracts_dir, self.contracts_dir, self.manifest_file)
        with open(self.manifest_file) as f:
            content = f.read()
        manifest_dict = loads(content)
        assert manifest_dict["manifest_version"] == "2"
        assert manifest_dict["version"] == "vyper"
        assert "./vyper/HelloWorld.vy" in manifest_dict["sources"].keys()
        assert manifest_dict["contract_types"]["HelloWorld"]["compiler"]["name"] == "vyper"

    def _copy_helloworld_vy(self):
        if not self.contracts_dir.exists():
            self.contracts_dir.mkdir()
        copy(self.fixtures_dir / "HelloWorld.vy", self.contracts_dir / "HelloWorld.vy")

    def _copy_helloworld_json(self):
        if not self.build_contracts_dir.exists():
            self.build_contracts_dir.mkdir()
        copy(self.fixtures_dir / "HelloWorld.json", self.build_contracts_dir / "HelloWorld.json")
