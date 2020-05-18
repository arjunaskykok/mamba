from sys import path
from pathlib import Path
from os import getcwd, environ

from web3 import Web3


class Contract:

    def __init__(self, settings_directory : Path = getcwd()):
        path.append(settings_directory)
        import settings
        networks = settings.networks

        infura_settings = settings.infura_settings
        if infura_settings:
            environ["WEB3_INFURA_PROJECT_ID"] = infura_settings["project_id"]
            environ["WEB3_INFURA_API_SECRET"] = infura_settings["project_secret"]

        development_network = networks["development"]
        if development_network["mode"]=="HTTP":
            server = "http://" + development_network["host"] + ":" + str(development_network["port"])
            self.w3 = Web3(Web3.HTTPProvider(server))
        elif development_network["mode"]=="IPC":
            ipc_url = development_network["url"]
            self.w3 = Web3(Web3.IPCProvider(ipc_url))
        elif development_network["mode"]=="Websocket":
            server = "ws://" + development_network["host"] + ":" + str(development_network["port"])
            self.w3 = Web3(Web3.WebsocketProvider(server))
        elif development_network["mode"]=="Infura":
            environ["WEB3_INFURA_SCHEME"] = str(development_network["scheme"])
            if development_network["endpoints"] == "mainnet":
                from web3.auto.infura.mainnet import w3
            elif development_network["endpoints"] == "ropsten":
                from web3.auto.infura.ropsten import w3
            elif development_network["endpoints"] == "goerli":
                from web3.auto.infura.goerli import w3
            elif development_network["endpoints"] == "rinkeby":
                from web3.auto.infura.rinkeby import w3
            elif development_network["endpoints"] == "kovan":
                from web3.auto.infura.kovan import w3
            self.w3 = w3
