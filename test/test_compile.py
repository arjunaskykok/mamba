from json import loads
from vyper import __version__ as version

from black_mamba.compilation.vyper_compiler import compile_all_files
from black_mamba.testlib.test_with_contracts import TestWithContracts


class TestCompile(TestWithContracts):

    def test_compile_vyper_file(self):
        compile_all_files(self.fixtures_dir, self.build_contracts_dir, self.migrations_dir)
        content = self.json_compiled_file.read_text()
        json_compiled_object = loads(content)
        assert json_compiled_object["contractName"]=="HelloWorld"
        assert json_compiled_object["bytecode"][0:10]=="0x600b6101"
        assert json_compiled_object["abi"][0]["type"]=="constructor"
        assert json_compiled_object["abi"][1]["name"]=="setGreeting"
        assert json_compiled_object["abi"][2]["name"]=="greet"
        assert json_compiled_object["compiler"]["name"]=="vyper"
        assert json_compiled_object["compiler"]["version"]==version
        assert json_compiled_object["opcodes"][0:5]=="PUSH1"
        assert json_compiled_object["opcodes_runtime"][0:5]=="CALLV"
        assert json_compiled_object["devdoc"]["methods"]["greet()"]["details"]=="Return the greeting which is 20 bytes"
        assert json_compiled_object["userdoc"]["notice"]=="You can use this contract for greeting"

        assert self.migration_file.exists()

    def test_compile_solidity_file(self):
        compile_all_files(self.fixtures_dir, self.build_contracts_dir, self.migrations_dir)
        content = self.solidity_json_compiled_file.read_text()
        json_compiled_object = loads(content)
        assert json_compiled_object["contractName"]=="SimpleStorage"
        assert json_compiled_object["bin"][0:10]=="6080604052"
        assert json_compiled_object["bin-runtime"][0:10]=="6080604052"
        assert json_compiled_object["abi"][0]["type"]=="function"
        assert json_compiled_object["compiler"]["name"]=="solidity"
        assert json_compiled_object["compiler"]["version"][0:3]=="0.8"
        assert json_compiled_object["opcodes"][0:5]=="PUSH1"

        assert self.solidity_migration_file.exists()
