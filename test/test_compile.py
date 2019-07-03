from pathlib import Path
from json import loads
from vyper import __version__ as version

from compilation.vyper_compiler import compile_all_files


class TestCompile():

    tmp_path = Path('/tmp') # TODO: Change this into dynamic temp directory

    def setup_method(self, method):
        self.fixtures_dir = Path('.') / Path('test') / Path('fixtures')
        self.build_dir = self.tmp_path / Path('build')
        self.build_contracts_dir = self.tmp_path / Path('build') / Path('contracts')
        self.json_compiled_file = self.build_contracts_dir / Path('HelloWorld.json')

        self.build_dir.mkdir()
        self.build_contracts_dir.mkdir()

    def teardown_method(self, method):
        self.json_compiled_file.unlink()
        self.build_contracts_dir.rmdir()
        self.build_dir.rmdir()

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
