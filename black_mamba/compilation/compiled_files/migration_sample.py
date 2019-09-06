from black_mamba.deploy import DeployContract


deploy_contract_instance = DeployContract()
parameters = []
tx_params = {{ "from": "" }}
private_key = None

deploy_contract_instance.deploy_contract("{smart_contract_name}", parameters, tx_params, private_key)
