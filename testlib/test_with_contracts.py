from pathlib import Path


class TestWithContracts():

    tmp_path = Path('/tmp') # TODO: Change this into dynamic temp directory

    def setup_method(self, method):
        self.fixtures_dir = Path('.') / Path('test') / Path('fixtures')
        self.build_dir = self.tmp_path / Path('build')
        self.build_contracts_dir = self.tmp_path / Path('build') / Path('contracts')
        self.json_compiled_fixture = self.fixtures_dir / Path("HelloWorld.json")
        self.json_compiled_file = self.build_contracts_dir / Path('HelloWorld.json')
        self.json2_compiled_fixture = self.fixtures_dir / Path("HelloParameters.json")
        self.json2_compiled_file = self.build_contracts_dir / Path('HelloParameters.json')

        self.build_dir.mkdir()
        self.build_contracts_dir.mkdir()

    def teardown_method(self, method):
        if self.json_compiled_file.exists():
            self.json_compiled_file.unlink()
        if self.json2_compiled_file.exists():
            self.json2_compiled_file.unlink()
        self.build_contracts_dir.rmdir()
        self.build_dir.rmdir()
