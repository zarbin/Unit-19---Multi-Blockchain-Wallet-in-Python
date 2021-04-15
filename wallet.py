import subprocess
import json
import os

from web3 import Web3   #Python Ethereum library
from bit import *  #Python Bitcoin library
from bit.network import NetworkAPI
from eth_account import Account #ethereum Account
from constants import *
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

#w3 provider
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

#Add the following middlewareto web3.py to support the PoA algorithm:
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#get mnemonic from .env
mnemonic = os.getenv("MNEMONIC_KEY", 'insert mnemonic here')

#check connection
w3.isConnected()

#check key
print(type(mnemonic))


#functions

# derive wallets function that uses hd-wallet-derive tool
def derive_wallets(mnemonic, coin, numderive):
    command = 'php ./derive -g --mnemonic="' + mnemonic + '" --numderive="' + str(numderive) + '" --cols=path,address,privkey,pubkey --coin="' + coin + '" --format=jsonpretty'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    return json.loads(output)

# private key to accound function
def priv_key_to_account (coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# create transaction function
def create_tx(coin, account, recipient, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        return {
            "from": account.address,   # DOUBLE CHECK THAT ACCOUNT.ADDRESS MAKES SENSE???
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            #AND CHAIN ID???
        }

    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])    #should be to or receipient??
    
# send transaction function
def send_tx(coin, account, recipient, amount):
    if coin == ETH:
        raw_tx  = create_tx(coin, account, recipient, amount)
        signed_tx = account.sign_transaction(raw_tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        raw_tx  = create_tx(coin,account,recipient,amount)
        signed_tx = account.sign_transaction(raw_tx)
        result = NetworkAPI.broadcast_tx_testnet(signed_tx)     
        print(result)  
        return result        

coins = {'eth':derive_wallets(mnemonic=mnemonic,coin=ETH,numderive=3),'btc-test': derive_wallets(mnemonic=mnemonic,coin=BTCTEST,numderive=3)}
print(coins)

# assign private keys from above to variables
eth_privatekey = coins['eth'][0]['privkey']
btc_privatekey = coins['btc-test'][0]['privkey']

print(eth_privatekey)
print(btc_privatekey)

eth_account = priv_key_to_account(ETH,eth_privatekey)
btc_account = priv_key_to_account(BTCTEST,btc_privatekey)

print(eth_account)
print(btc_account)

send_tx(BTCTEST, 'mhNGadXRRE4nCUVSHDb6oywJsNEKHMfeVp', '2NBw6PXYPrCYfyc1EKvkSgfrJ5N3PFyh7ts', .00588344)