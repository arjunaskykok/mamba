from argparse import ArgumentParser
from pathlib import Path

from black_mamba.initialization.init import initialize_project_directory
from black_mamba.compilation.vyper_compiler import compile_all_files
from black_mamba.server.geth_dev_server import run_server
from black_mamba.auth import Authentication
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

    pm_group = parser.add_argument_group('pm')
    pm_group.add_argument('--epm_mode', action="store", help="Mode of Ethereum package manager: install / list / uninstall / create", default="list")
    pm_group.add_argument('--epm_uri', action="store", default=None)
    pm_group.add_argument('--epm_package', action="store", default=None)

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


if __name__ == "__main__":
    parse_cli_args()
