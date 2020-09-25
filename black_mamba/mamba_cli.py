from argparse import ArgumentParser
from pathlib import Path
from subprocess import run

from black_mamba.initialization.init import initialize_project_directory
from black_mamba.compilation.vyper_compiler import compile_all_files
from black_mamba.server.geth_dev_server import run_server
from black_mamba.auth import Authentication
from black_mamba.mnemonic import Mnemonic
from black_mamba.epm.package_manager import PackageManager
from black_mamba.constants import ETHEREUM_PACKAGES_DIR


def parse_cli_args():

    parser = ArgumentParser(description="Mamba Framework")
    parser.add_argument('mode', type=str, help="Mode of Mamba CLI: init / compile / server / keyfile")
    parser.add_argument('--httpserver', action="store_true", default=False)
    parser.add_argument('--websocket', action="store_true", default=False)

    keyfile_group = parser.add_argument_group('keyfile')
    keyfile_group.add_argument('--keyfile_mode', action="store", help="encrypt or decrypt the keyfile", default=False)
    keyfile_group.add_argument('--keyfile_file', action="store", default=False)
    keyfile_group.add_argument('--keyfile_private_key', action="store", default=False)
    keyfile_group.add_argument('--keyfile_password', action="store", default=False)

    epm_group = parser.add_argument_group('epm')
    epm_help = """Mode of Ethereum package manager: install / list / uninstall / create.
    "install" -> Install package from GitHub or registry.
    "list" -> List all installed packages.
    "uninstall" -> Uninstall package.
    "create" -> Create a package manifest from the source code, ABI, and bytecode of the smart contract.
    "pin" -> Pin the package manifest to IPFS.
    """
    epm_group.add_argument('--epm_mode', action="store", help=epm_help, default="list")
    epm_group.add_argument('--epm_uri', action="store", default=None)
    epm_group.add_argument('--epm_package', action="store", default=None)

    mnemonic_group = parser.add_argument_group('generate_mnemonic')
    mnemonic_group.add_argument('--num_words', action="store", help="number of words in mnemonic (must be 12, 15, 18, 21, 24)", default=12)
    mnemonic_group.add_argument('--language', action="store", help="language to use (must be english, czech, french, italian, japanese, korean, spanish, chinese_simplified, chinese_traditional)", default="english")

    test_group = parser.add_argument_group('test')
    test_group.add_argument('--file', action="store", default=None)

    arguments = parser.parse_args()

    if arguments.mode=="init":
        initialize_project_directory(Path('.'))
    elif arguments.mode=="compile":
        compile_all_files(Path('contracts'), Path('build') / Path('contracts'), Path("migrations"))
    elif arguments.mode=="server":
        run_server(Path("datadir"), arguments.httpserver, arguments.websocket)
    elif arguments.mode=="keyfile":
        if arguments.keyfile_mode == "encrypt":
            Authentication.encrypt_keyfile(arguments.keyfile_file, arguments.keyfile_private_key, arguments.keyfile_password)
        elif arguments.keyfile_mode == "decrypt":
            Authentication.decrypt_keyfile(arguments.keyfile_file, arguments.keyfile_password)
    elif arguments.mode=="epm":
        epm = PackageManager(Path(ETHEREUM_PACKAGES_DIR))
        epm.operate(arguments.epm_mode, arguments.epm_uri, arguments.epm_package)
    elif arguments.mode=="generate_mnemonic":
        mnemonic = Mnemonic.generate_mnemonic(int(arguments.num_words), arguments.language)
        print(mnemonic)
    elif arguments.mode=="test":
        pytest_args = arguments.file.split(" ")
        run(["py.test", *pytest_args])


if __name__ == "__main__":
    parse_cli_args()
