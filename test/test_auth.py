from pathlib import Path
from io import StringIO
import sys

from black_mamba.auth import Authentication
from black_mamba.testlib.test_with_contracts import TestWithContracts
import pytest


class TestAuth(TestWithContracts):

    expected_private_key = "0bf89b27648bd7fb6ed5478a9865a05968f14b3644153adaa7d603f755a436f5"
    expected_private_key_mnemonic = "aba0a55ccb517ad219ee2f7f5d60b39379dcffbf6c6c9063830a15813a87e649"
    mnemonic = "coral allow abandon recipe top tray caught video climb similar prepare bracket antenna rubber announce gauge volume hub hood burden skill immense add acid"
    password = "password123"

    def test_get_private_key_from_keyfile_by_explicit_password(self):
        keyfile_path = self.fixtures_dir / Path("keyfile.json")
        private_key = Authentication.get_private_key_from_keyfile_by_explicit_password(str(keyfile_path), self.password)
        assert private_key == self.expected_private_key

    def test_get_private_key_from_keyfile_by_explicit_password_wrong_password(self):
        keyfile_path = self.fixtures_dir / Path("keyfile.json")
        with pytest.raises(ValueError):
            Authentication.get_private_key_from_keyfile_by_explicit_password(str(keyfile_path), "wrongpassword")

    def test_get_private_key_from_keyfile_by_asking_password(self, mocker):
        keyfile_path = self.fixtures_dir / Path("keyfile.json")
        mocker.patch("getpass.getpass", return_value=self.password)
        private_key = Authentication.get_private_key_from_keyfile_by_asking_password(str(keyfile_path))
        assert private_key == self.expected_private_key

    def test_encrypt_keyfile(self):
        keyfile2_path = self.tmp_path / Path("keyfile2.json")
        private_key2 = "cae245d529f9342eee882196c71ac6c720681e7e2d36a5509b6a0b946782c364"
        password2 = "abcdefgh"
        Authentication.encrypt_keyfile(keyfile2_path, private_key2, password2)
        extracted_private_key = Authentication.get_private_key_from_keyfile_by_explicit_password(str(keyfile2_path), password2)
        assert extracted_private_key == private_key2

    def test_decrypt_keyfile(self):
        keyfile_path = self.fixtures_dir / Path("keyfile.json")
        temp_out = StringIO()
        sys.stdout = temp_out
        Authentication.decrypt_keyfile(str(keyfile_path), self.password)
        assert temp_out.getvalue().rstrip() == self.expected_private_key
        sys.stdout = sys.__stdout__

    def test_get_private_key_from_mnemonic(self):
        private_key = Authentication.get_private_key_from_mnemonic(self.mnemonic)
        assert private_key == self.expected_private_key_mnemonic
