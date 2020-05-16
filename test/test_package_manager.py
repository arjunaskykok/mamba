from pathlib import Path
from shutil import copy
from contextlib import redirect_stdout
import io

import pytest

from black_mamba.epm.package_manager import PackageManager
from black_mamba.testlib.test_with_contracts import TestWithContracts
from black_mamba.constants import ETHEREUM_PACKAGES_DIR


class TestPackageManager(TestWithContracts):

    def setup_method(self, method):
        super().setup_method(method)
        self.packages_dir = self.tmp_path / Path(ETHEREUM_PACKAGES_DIR)
        self.parent_dir = self.packages_dir / "owned"
        self.version_dir = self.parent_dir / "1.0.1"
        self.manifest_file = self.version_dir / "manifest.json"
        self.epm = PackageManager(self.packages_dir)
        self.use_infura()

    def test_install(self):
        self._install()
        manifest_fixture = self.fixtures_dir / "manifest.json"
        with open(manifest_fixture) as f:
            fixture_content = f.read()
        with open(self.manifest_file) as f:
            content = f.read()
        assert fixture_content == content

    def test_list(self):
        self._install()
        f = io.StringIO()
        with redirect_stdout(f):
            self.epm.list()

        output = f.getvalue()
        f.close()
        assert output == "owned\n"

    def test_uninstall(self):
        self._install()
        self.epm.uninstall("owned")
        assert self.parent_dir.exists() == False

    def _install(self):
        uri = "https://api.github.com/repos/ethereum/web3.py/git/blobs/a7232a93f1e9e75d606f6c1da18aa16037e03480"
        self.epm.install(uri)

    def use_infura(self):
        copy(self.fixtures_dir / Path("infura_settings.py"), Path("settings.py"))

    def remove_infura_settings(self):
        if Path("settings.py").exists():
            Path("settings.py").unlink()

    def teardown_method(self, method):
        super().teardown_method(method)
        if self.manifest_file.exists():
            self.manifest_file.unlink()
        if self.version_dir.exists():
            self.version_dir.rmdir()
        if self.parent_dir.exists():
            self.parent_dir.rmdir()
        if self.packages_dir.exists():
            self.packages_dir.rmdir()
        self.remove_infura_settings()
