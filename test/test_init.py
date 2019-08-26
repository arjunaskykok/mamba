from pathlib import Path

from initialization.init import initialize_project_directory


class TestInit():

    tmp_path = Path('/tmp') # TODO: Change this into dynamic temp directory

    def setup_method(self, method):
        self.contracts_dir = self.tmp_path / Path('contracts')
        self.build_dir = self.tmp_path / Path('build')
        self.build_contracts_dir = self.tmp_path / Path('build/contracts')
        self.test_dir = self.tmp_path / Path('test')
        self.migrations_dir = self.tmp_path / Path("migrations")
        self.deployed_dir = self.tmp_path / Path("deployed")
        self.settings_file = self.tmp_path / Path("settings.py")

    def teardown_method(self, method):
        self.contracts_dir.rmdir()
        self.build_contracts_dir.rmdir()
        self.build_dir.rmdir()
        self.test_dir.rmdir()
        self.migrations_dir.rmdir()
        self.deployed_dir.rmdir()
        self.settings_file.unlink()

    def test_initialize_project_directory(self):
        initialize_project_directory(self.tmp_path)
        assert self.contracts_dir.exists()
        assert self.build_dir.exists()
        assert self.build_contracts_dir.exists()
        assert self.test_dir.exists()
        assert self.migrations_dir.exists()
        assert self.deployed_dir.exists()
        assert self.settings_file.exists()
