from pathlib import Path
from json import load

from black_mamba.constants import SMART_CONTRACT_BUILD_DIR


class BuildContract:

    build_contract = {}

    def __init__(self,
                 smart_contract_name : str,
                 build_contracts_directory : Path = SMART_CONTRACT_BUILD_DIR):
        contract_json_file = (build_contracts_directory / smart_contract_name).with_suffix('.json')

        with open(contract_json_file, "r") as smart_contract_build_file:
            self.build_contract = load(smart_contract_build_file)
