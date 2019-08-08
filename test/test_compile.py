from json import loads
from vyper import __version__ as version

from compilation.vyper_compiler import compile_all_files
from testlib.test_with_contracts import TestWithContracts


class TestCompile(TestWithContracts):

    def test_compile_vyper_file(self):
        compile_all_files(self.fixtures_dir, self.build_contracts_dir)
        content = self.json_compiled_file.read_text()
        json_compiled_object = loads(content)
        assert json_compiled_object['contractName']=='HelloWorld'
        assert json_compiled_object['bytecode'][0:10]=='0x74010000'
        assert json_compiled_object['abi'][0]['type']=='constructor'
        assert json_compiled_object['abi'][1]['name']=='setGreeting'
        assert json_compiled_object['abi'][2]['name']=='greet'
        assert json_compiled_object['compiler']['name']=='vyper'
        assert json_compiled_object['compiler']['version']==version
