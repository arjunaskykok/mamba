from pathlib import Path
from shutil import copyfile


def initialize_project_directory(current_directory: Path):
    contracts_dir = current_directory / Path('contracts')
    contracts_dir.mkdir()

    build_dir = current_directory / Path('build')
    build_dir.mkdir()
    build_contracts_dir = current_directory / Path('build') / Path('contracts')
    build_contracts_dir.mkdir()

    test_dir = current_directory / Path('test')
    test_dir.mkdir()

    migrations_dir = current_directory / Path("migrations")
    migrations_dir.mkdir()

    deployed_dir = current_directory / Path('deployed')
    deployed_dir.mkdir()

    decentralized_app_dir = current_directory / Path('decentralized_app')
    decentralized_app_dir.mkdir()

    settings_sample = Path(__file__).parent / Path("init_files") / Path("settings_sample.py")
    settings_file = current_directory / Path("settings.py")
    copyfile(settings_sample, settings_file)
