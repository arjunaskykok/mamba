from os import environ


networks = {
    "development": {
        "mode": "HTTP",
        "host": "localhost",
        "port": 7545,
        "network_id": "*"
    }
}

infura_settings = {
    "project_id": environ["PROJECT_ID"],
    "project_secret": environ["PROJECT_SECRET"],
}
