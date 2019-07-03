from argparse import ArgumentParser
from pathlib import Path

from initialization.init import initialize_project_directory
from compilation.vyper_compiler import compile_all_files


parser = ArgumentParser(description="Mamba Framework")
parser.add_argument('mode', type=str, help="mode of Mamba tool")

args = parser.parse_args()

mode = args.mode
if mode == 'init':
    initialize_project_directory(Path('.'))
elif mode == 'compile':
    compile_all_files(Path('contracts'), Path('build') / Path('contracts'))
