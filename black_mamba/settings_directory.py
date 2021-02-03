from sys import path
from pathlib import Path
from os import getcwd


settings_directory : Path = getcwd()
path.append(settings_directory)
