import requests

from black_mamba import settings_directory
import settings

etherscan = settings.etherscan

api_key = etherscan["development"]["api_key"]

server = 'https://api.etherscan.io'


def ether_balance_multi(account_addresses):
    """Getting the balances of ETH of accounts

    Parameters
    ----------
    account_addresses : array of str
      The addresses of the accounts
    """
    account_addresses_string = ",".join(account_addresses)
    response = requests.get(f'{server}/api?module=account&action=balancemulti&address={account_addresses_string}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def ether_balance_single(account_address):
    """Getting the balance of ETH of an account

    Parameters
    ----------
    account_address : str
      The address of the account
    """
    response = requests.get(f'{server}/api?module=account&action=balance&address={account_address}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def normal_transactions(account_address, startblock=0, endblock=99999999, sort="asc"):
    """Getting the list of normal transactions

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=txlist&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def normal_transactions_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    """Getting the list of normal transactions (pagination version)

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=txlist&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions(account_address, startblock=0, endblock=99999999, sort="asc"):
    """Getting the list of internal transactions

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    """Getting the list of internal transactions (pagination version)

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_transaction_hash(txhash):
    """Getting the list of internal transactions by transaction hash

    Parameters
    ----------
    txhash : str
      The transaction hash
    """
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&txhash={txhash}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def internal_transactions_block_range(startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    """Getting the list of internal transactions by block range

    Parameters
    ----------
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=txlistinternal&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events(account_address, startblock=0, endblock=99999999, sort="asc"):
    """Getting the list of ERC-20 token transfer events

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokentx&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    """Getting the list of ERC-20 token transfer events (pagination version)

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokentx&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_token_transfer_events_contract_address(contract_address, account_address, page=1, offset=10, sort="asc"):
    """Getting the list of ERC-20 token transfer events with a smart contract's address

    Parameters
    ----------
    contract_address : str
      The address of the ERC-20 token smart contract
    account_address : str
      The address of the account
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events(account_address, startblock=0, endblock=99999999, sort="asc"):
    """Getting the list of ERC-721 token transfer events

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&address={account_address}&startblock={startblock}&endblock={endblock}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events_paginated(account_address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
    """Getting the list of ERC-721 token transfer events (pagination version)

    Parameters
    ----------
    account_address : str
      The address of the account
    startblock : int, optional
      The start of the block number (default is 0)
    endblock : int, optional
      The end of the block number (default is 99999999)
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&address={account_address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc721_token_transfer_events_contract_address(contract_address, account_address, page=1, offset=10, sort="asc"):
    """Getting the list of ERC-721 token transfer events with a smart contract's address

    Parameters
    ----------
    contract_address : str
      The address of the ERC-721 token smart contract
    account_address : str
      The address of the account
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    sort : str, optional
      The way of the result is sorted, "asc" or "desc" (default is "asc")
    """
    response = requests.get(f'{server}/api?module=account&action=tokennfttx&contractaddress={contract_address}&address={account_address}&page={page}&offset={offset}&sort={sort}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def blocks_mined(account_address):
    """Getting the list of block mined by an account

    Parameters
    ----------
    account_address : str
      The address of the account
    """
    response = requests.get(f'{server}/api?module=account&action=getminedblocks&address={account_address}&blocktype=blocks&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def blocks_mined_paginated(account_address, page=1, offset=10):
    """Getting the list of block mined by an account (pagination version)

    Parameters
    ----------
    account_address : str
      The address of the account
    page : int, optional
      The page number (default is 1)
    offset : int, optional
      Maximum records to be returned (default is 10)
    """
    response = requests.get(f'{server}/api?module=account&action=getminedblocks&address={account_address}&blocktype=blocks&page={page}&offset={offset}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]
