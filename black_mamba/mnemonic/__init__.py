from eth_account import hdaccount


class Mnemonic:

    @staticmethod
    def generate_mnemonic(num_words: int, lang: str) -> str:
        return hdaccount.generate_mnemonic(num_words, lang)
