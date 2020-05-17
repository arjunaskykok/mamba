from json import dumps
from pathlib import Path
from typing import Dict, Tuple

from black_mamba.constants import SMART_CONTRACT_BUILD_DIR, SMART_CONTRACT_SOURCE_DIR
from black_mamba.contract.build_contract import BuildContract


def operate_manifest():
    create_contract_types()

def ask_meta_from_user() -> Dict:
    print("Please answer these questions for meta!")
    authors_string = input("Authors (separate them by comma), e.g. Arjuna <arjuna@mamba.black>: ")
    authors = list(map(lambda x: x.strip(), authors_string.split(", ")))
    description = input("Description: ")
    keywords_string = input("Keywords (separate them by comma): ")
    keywords = list(map(lambda x: x.strip(), keywords_string.split(", ")))
    license = input("License: ")
    documentation = input("Documentation URL: ")
    repo = input("Repository: ")
    website = input("Website: ")
    return {
        "authors": authors,
        "description": description,
        "keywords": keywords,
        "license": license,
        "links": {
            "documentation": documentation,
            "repo": repo,
            "website": website
        }
    }

def ask_package_version_from_user() -> Tuple:
    print("Please answer these questions for package and version!")
    package = input("Package name: ")
    version = input("Version: ")
    return (package, version)

def create_contract_types(build_contracts_directory : Path = SMART_CONTRACT_BUILD_DIR) -> Dict:
    contract_types_dict = {
    }

    for smart_contract in build_contracts_directory.iterdir():
        if not smart_contract.name.startswith("."):
            contract_type = {}
            build_contract_object = BuildContract(smart_contract.name, build_contracts_directory)
            build_contract = build_contract_object.build_contract
            contract_type["abi"] = build_contract["abi"]
            contract_type["compiler"] = {
                "name": build_contract["compiler"]["name"],
                "settings": {"optimize": False},
                "version": build_contract["compiler"]["version"]
            }
            contract_type["deployment_bytecode"] = {
                "bytecode": build_contract["bytecode"]
            }
            if build_contract["devdoc"]:
                contract_type["natspec"] = {
                    "details": build_contract["devdoc"]["details"],
                    "methods": build_contract["devdoc"]["methods"]
                }
            contract_type["runtime_bytecode"] = {
                "bytecode": build_contract["bytecode_runtime"]
            }
            contract_types_dict[smart_contract.name[:-5]] = contract_type

    return contract_types_dict

def create_sources(package_name: str, source_contracts_directory : Path = SMART_CONTRACT_SOURCE_DIR) -> Dict:
    sources = {
    }

    for smart_contract in source_contracts_directory.iterdir():
        if not smart_contract.name.startswith("."):
            source_key = f"./{package_name}/{smart_contract.name}"
            with open(smart_contract, "r") as f:
                content = f.read()
                sources[source_key] = content

    return sources

def create_manifest(contract_types: Dict, meta: Dict, package_name: str, sources: Dict, version: str) -> Dict:
    manifest = {
        "contract_types": contract_types,
        "manifest_version": 2,
        "meta": meta,
        "package_name": package_name,
        "sources": sources,
        "version": version
    }
    return manifest

def write_manifest(manifest_dict: Dict, json_file: Path):
    package_version = ask_package_version_from_user()
    package_name = package_version[0]
    version = package_version[1]
    meta = ask_meta_from_user()
    sources = create_sources(package_name)
    contract_types = create_contract_types()
