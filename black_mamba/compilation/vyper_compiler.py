from pathlib import Path
from json import dump
from vyper import compile_codes, __version__ as version


def compile_all_files(source_code_directory: Path, build_directory: Path, migration_directory: Path):
    vyper_files = source_code_directory.glob("*.vy")
    for vyper_file in vyper_files:
        with open(vyper_file, 'r') as f:
            build_dir_str = str(build_directory)
            smart_contract_name = Path(vyper_file).with_suffix('').name
            content = f.read()

            smart_contract = {}
            smart_contract[build_dir_str] = content

            formats = ["abi", "bytecode", "ast_dict", "external_interface", "interface", "method_identifiers", "asm", "source_map",
                      "bytecode_runtime", "opcodes", "opcodes_runtime", "devdoc", "userdoc"]
            compiled_code = compile_codes(smart_contract, formats, 'dict')

            smart_contract_json = {
                "contractName": smart_contract_name,
                "compiler": { "name": "vyper",
                              "version": version
                            }
            }

            for format in formats:
                smart_contract_json[format] = compiled_code[build_dir_str][format]

            contract_json_file = build_dir_str + '/' + smart_contract_name + '.json'
            with open(contract_json_file, 'w') as smart_contract_build_file:
                dump(smart_contract_json, smart_contract_build_file, indent=4)

            migration_sample = Path(__file__).parent / Path("compiled_files") / Path("migration_sample.py")
            prefix_deploy_file = "deploy_"
            migration_file_name = f"{prefix_deploy_file}{smart_contract_name}.py"
            migration_file = migration_directory / Path(migration_file_name)
            with open(migration_file, "w") as file:
                migration_sample_content = migration_sample.read_text()
                content = migration_sample_content.format(smart_contract_name=smart_contract_name)
                file.write(content)
