from black_mamba.testlib.test_with_contracts import TestWithContracts
from black_mamba.mnemonic import Mnemonic


class TestMnemonic(TestWithContracts):

    def test_generate_mnemonic(self):
        mnemonic = Mnemonic.generate_mnemonic(12, "english")
        result = mnemonic.split(" ")
        assert len(result) == 12
