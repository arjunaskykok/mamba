from pathlib import Path
from shutil import rmtree


class TestWithContracts():

    tmp_path = Path('/tmp/mamba_tests/') # TODO: Change this into dynamic temp directory

    def setup_method(self, method):
        self.tmp_path.mkdir()
        self.fixtures_dir = Path('.') / Path('test') / Path('fixtures')
        self.build_dir = self.tmp_path / Path('build')
        self.migrations_dir = self.tmp_path / Path("migrations")
        self.decentralized_app_dir = self.tmp_path / Path("decentralized_app")
        self.contracts_dir = self.tmp_path / Path("contracts")
        self.build_contracts_dir = self.tmp_path / Path('build') / Path('contracts')
        self.json_compiled_fixture = self.fixtures_dir / Path("HelloWorld.json")
        self.json_compiled_file = self.build_contracts_dir / Path('HelloWorld.json')
        self.migration_file = self.migrations_dir / Path("deploy_HelloWorld.py")
        self.migration2_file = self.migrations_dir / Path("deploy_HelloParameters.py")
        self.json2_compiled_fixture = self.fixtures_dir / Path("HelloParameters.json")
        self.json2_compiled_file = self.build_contracts_dir / Path('HelloParameters.json')
        self.keyfile2_file = self.tmp_path / Path('keyfile2.json')
        self.manifest_file = self.tmp_path / Path("manifest.json")

        if not self.build_dir.exists():
            self.build_dir.mkdir()
        if not self.build_contracts_dir.exists():
            self.build_contracts_dir.mkdir()
        if not self.migrations_dir.exists():
            self.migrations_dir.mkdir()
        if not self.decentralized_app_dir.exists():
            self.decentralized_app_dir.mkdir()

    def teardown_method(self, method):
        rmtree(self.tmp_path)
