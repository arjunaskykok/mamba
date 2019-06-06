from argparse import ArgumentParser

from initialization.init import initialize_project_directory


parser = ArgumentParser(description="Mamba Framework")
parser.add_argument('mode', type=str, help="mode of Mamba tool")

args = parser.parse_args()

mode = args.mode
if mode == 'init':
    initialize_project_directory(Path('.'))
