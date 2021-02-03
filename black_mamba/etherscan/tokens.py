import requests

from black_mamba import settings_directory
import settings

etherscan = settings.etherscan

api_key = etherscan["development"]["api_key"]

server = 'https://api.etherscan.io'


def erc20_total_supply(contract_address):
    response = requests.get(f'{server}/api?module=stats&action=tokensupply&contractaddress={contract_address}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_account_balance(contract_address, account_address):
    response = requests.get(f'{server}/api?module=account&action=tokenbalance&contractaddress={contract_address}&address={account_address}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def ether_balance_multi(account_addresses):
    account_addresses_string = ",".join(account_addresses)
    response = requests.get(f'{server}/api?module=account&action=balancemulti&address={account_addresses_string}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def ether_balance_single(account_address):
    response = requests.get(f'{server}/api?module=account&action=balance&address={account_address}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def normal_transactions(account_address, startblock=0, endblock=99999999, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=txlist&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def normal_transactions_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=txlist&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions(account_address, startblock=0, endblock=99999999, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_transaction_hash(txhash):
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&txhash={txhash}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_block_range(startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events(account_address, startblock=0, endblock=99999999, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokentx&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokentx&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events_contract_address(contract_address, account_address, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events(account_address, startblock=0, endblock=99999999, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events_contract_address(contract_address, account_address, page=1, offset=10, sort="asc"):
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&contractaddress={contract_address}&address={account_address}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def blocks_mined(account_address):
    response = requests.get(f'{server}/api?module=account&action=getminedblocks&address={account_address}&blocktype=blocks&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def blocks_mined_paginated(account_address, page=1, offset=10):
    response = requests.get(f'{server}/api?module=account&action=getminedblocks&address={account_address}&blocktype=blocks&page={page}&offset={offset}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]
