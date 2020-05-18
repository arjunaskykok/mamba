import os


networks = {
    "development": {
        "mode": "HTTP",
        "host": "localhost",
        "port": 7545,
        "network_id": "*"
    }

    #"development": {
    #    "mode": "IPC",
    #    "url": "/home/sarahconnor/ethereum/data/geth.ipc"
    #}

    #"development": {
    #    "mode": "Websocket",
    #    "host": "localhost",
    #    "port": 8546,
    #    "network_id": "*"
    #}

    #"development": {
    #    "mode": "IPC",
    #    "url": "/home/sarahconnor/ethereum/data/geth.ipc"
    #}

    #"development": {
    #    "mode": "Infura",
    #    "scheme": "https / wss",
    #    "endpoints": "mainnet / ropsten / goerly / rinkeby / kovan"
    #}
}

infura_settings = {
    "project_id": "FILL_IT_WITH_PROJECT_ID",
    "project_secret": "FILL_IT_WITH_PROJECT_SECRET",
}

auth = {
    "development": {
        #"private_key": os.environ("MY_PRIVATE_KEY")
        "password": "password_to_unlock_keyfile",
        "keyfile": "keyfile.json"
    }
}
