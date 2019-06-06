from pathlib import Path


def initialize_project_directory(current_directory: Path):
    contracts_dir = current_directory / Path('contracts')
    contracts_dir.mkdir()

    build_dir = current_directory / Path('build')
    build_dir.mkdir()
    build_contracts_dir = current_directory / Path('build') / Path('contracts')
    build_contracts_dir.mkdir()

    test_dir = current_directory / Path('test')
    test_dir.mkdir()

    deployments_dir = current_directory / Path('deployments')
    deployments_dir.mkdir()
