from json import dumps
from pathlib import Path

from ethpm import Package
from black_mamba.contract.contract import Contract


class PackageManager:

    def __init__(self, packages_dir: str):
        """
        A package manager's purpose is to install, remove, list packages from chain or files.
        """
        self.packages_dir = packages_dir

    def operate(self, mode: str, uri: str, package: str):
        """
        Convenient method called from Mamba CLI.
        """
        if mode=="install":
            self.install(uri)
        elif mode=="list":
            self.list()
        elif mode=="remove":
            pass
        elif mode=="create":
            pass

    def install(self, uri: str):
        """
        Install packages from chain or files and put it in packages directory.
        """
        self._create_ethpm_packages_dir()

        contract_instance = Contract()
        w3 = contract_instance.w3

        is_file = True
        for prefix in ("ipfs://", "https://", "ethpm://", "erc1319://"):
            if uri.startswith(prefix):
                is_file = False
                break

        if is_file:
            package = Package.from_file(Path(uri), w3)
        else:
            package = Package.from_uri(uri, w3)

        self._write_manifests_to_filesystem(package.name, package.version, package.manifest)

    def list(self):
        """
        List installed packages.
        """
        packages_list = list(map(lambda x: x.name, self.packages_dir.iterdir()))
        print(*packages_list, sep="\n")

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
        manifest_content = dumps(manifest)
        manifest_file = version_dir / Path("manifest.json")
        with open(manifest_file, "w") as f:
            f.write(manifest_content)
