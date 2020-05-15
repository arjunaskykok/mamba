from os import environ


networks = {
    "development": {
        "mode": "Infura",
        "project_id": environ["PROJECT_ID"],
        "api_secret": environ["API_SECRET"],
        "scheme": "https",
        "endpoints": "mainnet"
    }
}
