from os import environ


networks = {
    "development": {
        "mode": "HTTP",
        "host": "localhost",
        "port": 7545,
        "network_id": "*"
    }
}

try:
    infura_settings = {
        "project_id": environ["PROJECT_ID"],
        "project_secret": environ["PROJECT_SECRET"],
    }
except:
    infura_settings = {
        "project_id": None,
        "project_secret": None,
    }

ipfs_settings = {
    "address": "/ip4/127.0.0.1/tcp/5001"          # Local IPFS node
}
