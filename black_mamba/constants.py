from pathlib import Path


ETHEREUM_PACKAGES_DIR = "ethpm_packages"
SMART_CONTRACT_BUILD_DIR = Path(".") / Path("build") / Path("contracts")
SMART_CONTRACT_SOURCE_DIR = Path(".") / Path("contracts")
EPM_BUILD_DIR = Path(".") / Path("ethpm_build")
MANIFEST_BUILD_FILE = EPM_BUILD_DIR / Path("manifest.json")
