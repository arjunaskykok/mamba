from subprocess import Popen, PIPE
from pathlib import Path
from shutil import copyfile


def setup_datadir(datadir: Path):
    if not datadir.exists():
        datadir.mkdir()

    genesis_sample = Path(__file__).parent / Path("server_files") / Path("genesis.json")
    genesis_file = datadir / Path("genesis.json")
    copyfile(genesis_sample, genesis_file)

    private_key_sample = Path(__file__).parent / Path("server_files") / Path("private_key.json")
    private_key_file = datadir / Path("private_key.json")
    copyfile(private_key_sample, private_key_file)

def check_geth_process():
    try:
        geth_process = Popen(["geth", "version"], stdout=PIPE, stderr=PIPE)
    except FileNotFoundError:
        return False
    stdout, _ = geth_process.communicate()
    if stdout.split(b"\n")[0] == b"Geth":
        return True
    return False

def check_datadir_inited(datadir: Path):
    geth_folder = datadir / Path("geth")
    keystore_folder = datadir / Path("keystore")
    if geth_folder.exists() and keystore_folder.exists():
        return True
    return False

def init_geth_datadir(datadir: Path):
    geth_process = Popen(["geth", "--datadir", ".", "init", "genesis.json"], cwd=datadir)
    geth_process.communicate()

def run_dev_server(datadir: Path, httpserver: bool, websocket: bool):
    geth_command = ["geth", "--networkid", "15", "--datadir", ".", "--mine", "--minerthreads", "1",
                    "--etherbase", "0x3333333333333333333333333333333333333333",
                    "--targetgaslimit", "10000000"]
    if httpserver:
        geth_command.extend(["--rpc"])
    if websocket:
        geth_command.extend(["--ws"])
    geth_process = Popen(geth_command, cwd=datadir)
    geth_process.communicate()

def run_server(datadir: Path, httpserver: bool, websocket: bool):
    setup_datadir(datadir)
    if not check_geth_process():
        print("You need to install Geth and put it in PATH.")
        print("Geth can be downloaded from here: https://geth.ethereum.org/downloads")
        return
    if not check_datadir_inited(datadir):
        init_geth_datadir(datadir)
    run_dev_server(datadir, httpserver, websocket)
