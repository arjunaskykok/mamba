from argparse import ArgumentParser
from pathlib import Path

from black_mamba.initialization.init import initialize_project_directory
from black_mamba.compilation.vyper_compiler import compile_all_files
from black_mamba.server.geth_dev_server import run_server


def parse_cli_args():

    parser = ArgumentParser(description="Mamba Framework")
    parser.add_argument('mode', type=str, help="mode of Mamba tool")
    parser.add_argument('--httpserver', action="store_true", required=False)
    parser.add_argument('--websocket', action="store_true", required=False)

    arguments = parser.parse_args()

    mode = arguments.mode
    if mode == 'init':
        initialize_project_directory(Path('.'))
    elif mode == 'compile':
        compile_all_files(Path('contracts'), Path('build') / Path('contracts'), Path("migrations"))
    elif mode == "server":
        run_server(Path("datadir"), arguments.httpserver, arguments.websocket)


if __name__ == "__main__":
    parse_cli_args()
