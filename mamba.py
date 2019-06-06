from argparse import ArgumentParser

parser = ArgumentParser(description='Mamba Framework')
parser.add_argument('mode', type=str, help='mode of Mamba tool')

args = parser.parse_args()
print(args.mode)
