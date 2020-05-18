from json import dumps, loads
from pathlib import Path
from shutil import rmtree
from os import getcwd

from typing import List

from ethpm import Package
from black_mamba.contract.contract import Contract
from black_mamba.epm.manifest import write_manifest


class PackageManager:

    def __init__(self, packages_dir: Path = Path(getcwd()) / Path("ethpm_packages")):
        """
        A package manager's purpose is to install, remove, list packages from chain or files.
        """
        self.packages_dir = packages_dir
        self.w3 = None

    def operate(self, mode: str, uri: str, package: str):
        """
        Convenient method called from Mamba CLI.
        """
        if mode=="install":
            self.install(uri)
        elif mode=="list":
            self.list()
        elif mode=="uninstall":
            self.uninstall(package)
        elif mode=="create":
            pass
            #write_manifest()

    def install(self, uri: str):
        """
        Install packages from chain or files and put it in packages directory.
        """
        self._create_ethpm_packages_dir()
        self._initialize_w3()

        is_file = True
        for prefix in ("ipfs://", "https://", "ethpm://", "erc1319://"):
            if uri.startswith(prefix):
                is_file = False
                break

        if is_file:
            package = Package.from_file(Path(uri), self.w3)
        else:
            package = Package.from_uri(uri, self.w3)

        self._write_manifests_to_filesystem(package.name, package.version, package.manifest)
        self.package = package

    def list(self):
        """
        List installed packages.
        """
        packages_list = list(map(lambda x: x.name, self.packages_dir.iterdir()))
        print(*packages_list, sep="\n")

    def uninstall(self, package_delete: str):
        """
        Remove an installed package.
        """
        for package_dir in self.packages_dir.iterdir():
            if package_dir.name == package_delete:
                rmtree(package_dir)
                print(f"Deleted {package_delete}")

    def load(self, contract_factory: str, package: Path, version: str = ""):
        """
        Load an installed package.
        """
        package_path = self.packages_dir / Path(package)
        versions = list(map(lambda p: p.name, package_path.iterdir()))
        if not version:
            version = self.find_max_version(versions)
        manifest_path = package_path / Path(version) / Path("manifest.json")

        self._initialize_w3()

        self.package = Package.from_file(manifest_path, self.w3)
        factory = self.package.get_contract_factory(contract_factory)

        factory.web3 = self.w3

        return factory

    def get_abi(self, contract_factory: str, package: Path, version: str = ""):
        """
        Get abi from the manifest file
        """
        package_path = self.packages_dir / Path(package)
        versions = list(map(lambda p: p.name, package_path.iterdir()))
        if not version:
            version = self.find_max_version(versions)
        manifest_path = package_path / Path(version) / Path("manifest.json")

        with open(manifest_path) as f:
            content = f.read()
        manifest = loads(content)
        abi = manifest["contract_types"][contract_factory]["abi"]

        return abi

    def _create_ethpm_packages_dir(self):
        if not self.packages_dir.exists():
            self.packages_dir.mkdir()

    def _write_manifests_to_filesystem(self, name: str, version: str, manifest: str):
        package_dir = self.packages_dir / Path(name)
        if not package_dir.exists():
            package_dir.mkdir()
        version_dir = package_dir / Path(version)
        if not version_dir.exists():
            version_dir.mkdir()
        manifest_content = dumps(manifest, sort_keys=True, separators=(",", ":"))
        manifest_file = version_dir / Path("manifest.json")
        with open(manifest_file, "w") as f:
            f.write(manifest_content)

    def _initialize_w3(self):
        contract_instance = Contract()
        self.w3 = contract_instance.w3

    def find_max_version(self, versions: List) -> str:
        """
        Given ["1.2.3", "3.2.11", "3.2.7", "2.0.0"], this method would return "3.2.11"
        """
        maximum = None

        def conv_to_int_arr(v):
            return list(map(lambda x: int(x), v.split(".")))

        if len(versions) == 0:
            return ""

        for version in versions:
            int_version = conv_to_int_arr(version)

            if len(int_version) == 1:
                int_version = [int_version[0], 0, 0]
            elif len(int_version) == 2:
                int_version = [int_version[0], int_version[1], 0]

            if maximum == None:
                maximum = int_version
            else:
                if maximum[0] > int_version[0]:
                    continue
                elif maximum[1] > int_version[1]:
                    continue
                elif maximum[2] > int_version[2]:
                    continue
                else:
                    maximum = int_version

        max_version = ".".join(map(lambda x: str(x), maximum))
        return max_version
