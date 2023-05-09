import os
from brownie import *

# set up Brownie and connect to Binance Smart Chain testnet
network.connect("bsc-testnet")
account = accounts.add(os.environ["PRIVATE_KEY"])

# set up BscScan API key
api_key = os.environ["BSCSCAN_API_KEY"]
network.verify = True
network.verify_contract = True
network.contract_verification_api_key = api_key

# find all Solidity files with ".sol" extension in a given folder
folder_path = "contracts"
folder_path = "/path/to/folder"
solidity_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".sol"):
            solidity_files.append(os.path.join(root, file))
            
# deploy each smart contract to Binance Smart Chain testnet and verify it on BscScan
for file_name in solidity_files:
    contract_name = os.path.splitext(file_name)[0]
    contract = compile_source_file(os.path.join(folder_path, file_name)).Vyper
    deployed_contract = contract.deploy({"from": account})
    deployed_contract.set_alias(contract_name)
    print(
        f"{contract_name} deployed to Binance Smart Chain testnet at {deployed_contract.address}"
    )
    network.verify(deployed_contract, api_key=api_key)
