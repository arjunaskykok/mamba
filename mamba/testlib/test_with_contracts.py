from pathlib import Path


class TestWithContracts():

    tmp_path = Path('/tmp') # TODO: Change this into dynamic temp directory

    def setup_method(self, method):
        self.fixtures_dir = Path('.') / Path('test') / Path('fixtures')
        self.build_dir = self.tmp_path / Path('build')
        self.migrations_dir = self.tmp_path / Path("migrations")
        self.decentralized_app_dir = self.tmp_path / Path("decentralized_app")
        self.build_contracts_dir = self.tmp_path / Path('build') / Path('contracts')
        self.json_compiled_fixture = self.fixtures_dir / Path("HelloWorld.json")
        self.json_compiled_file = self.build_contracts_dir / Path('HelloWorld.json')
        self.migration_file = self.migrations_dir / Path("deploy_HelloWorld.py")
        self.migration2_file = self.migrations_dir / Path("deploy_HelloParameters.py")
        self.json2_compiled_fixture = self.fixtures_dir / Path("HelloParameters.json")
        self.json2_compiled_file = self.build_contracts_dir / Path('HelloParameters.json')

        if not self.build_dir.exists():
            self.build_dir.mkdir()
        if not self.build_contracts_dir.exists():
            self.build_contracts_dir.mkdir()
        if not self.migrations_dir.exists():
            self.migrations_dir.mkdir()
        if not self.decentralized_app_dir.exists():
            self.decentralized_app_dir.mkdir()

    def teardown_method(self, method):
        if self.json_compiled_file.exists():
            self.json_compiled_file.unlink()
        if self.json2_compiled_file.exists():
            self.json2_compiled_file.unlink()
        if self.migration_file.exists():
            self.migration_file.unlink()
        if self.migration2_file.exists():
            self.migration2_file.unlink()
        if self.build_contracts_dir.exists():
            self.build_contracts_dir.rmdir()
        if self.build_dir.exists():
            self.build_dir.rmdir()
        if self.migrations_dir.exists():
            self.migrations_dir.rmdir()
        if self.decentralized_app_dir.exists():
            self.decentralized_app_dir.rmdir()
