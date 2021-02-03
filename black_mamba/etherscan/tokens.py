import requests

from black_mamba import settings_directory
import settings

etherscan = settings.etherscan

api_key = etherscan["development"]["api_key"]

server = 'https://api.etherscan.io'


def erc20_total_supply(contract_address):
    """Getting the total supply of ERC-20 token

    Parameters
    ----------
    contract_address : str
      The address of the ERC-20 token smart contract
    """
    response = requests.get(f'{server}/api?module=stats&action=tokensupply&contractaddress={contract_address}&apikey={api_key}')
    if response.ok:
        return response.json()["result"]

def erc20_account_balance(contract_address, account_address):
    """Getting the balance of ERC-20 token of an account

    Parameters
    ----------
    contract_address : str
      The address of the ERC-20 token smart contract
    account_address : str
      The address of the account
    """
    response = requests.get(f'{server}/api?module=account&action=tokenbalance&contractaddress={contract_address}&address={account_address}&tag=latest&apikey={api_key}')
    if response.ok:
        return response.json()["result"]
