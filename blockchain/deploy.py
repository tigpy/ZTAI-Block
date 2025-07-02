from web3 import Web3
import json

# Connect to local Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
assert w3.isConnected(), 'Web3 not connected!'

# Load compiled contract ABI and bytecode
with open('AccessLogger.abi.json') as f:
    abi = json.load(f)
with open('AccessLogger.bin', 'r') as f:
    bytecode = f.read().strip()

# Set deployer account
acct = w3.eth.accounts[0]

# Deploy contract
AccessLogger = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = AccessLogger.constructor().transact({'from': acct})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print('Contract deployed at:', tx_receipt.contractAddress)
