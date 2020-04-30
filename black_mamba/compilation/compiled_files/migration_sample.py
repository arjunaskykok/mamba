from sys import path
from os import getcwd

from black_mamba.deploy import DeployContract
from black_mamba.auth import Authentication


path.append(getcwd())
import settings
auth = settings.auth
development_auth = auth["development"]

keyfile = development_auth["keyfile"]
password = development_auth["password"]

private_key = Authentication.get_private_key_from_keyfile_by_explicit_password(keyfile, password)
# private_key = Authentication.get_private_key_from_keyfile_by_asking_password(keyfile)
# private_key = development_auth["private_key"]

deploy_contract_instance = DeployContract()
parameters = []
tx_params = {{ "from": "" }}

deploy_contract_instance.deploy_contract("{smart_contract_name}", parameters, tx_params, private_key)
