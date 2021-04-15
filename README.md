# Unit-19-Multi-Blockchain-Wallet-in-Python

# Background
Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.

You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.

Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.

In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.

# Requirements

Please see [Requirements](https://github.com/zarbin/Unit-19---Multi-Blockchain-Wallet-in-Python/blob/main/requirements.txt).

# Test Transactions
TEST transaction screenshots, as well as the code used to send them.

My Wallet was created successfully and I loaded BTC from Bitcoin testnet3 faucet found here: https://coinfaucet.eu/en/btc-testnet/
The faucet in the instructions did not work for me. 

Wallet Setup
![Screenshot](/images/walletsetup.png)

Send Transaction
![Screenshot](/images/sendtrans.png)

# Instructions
Write a short description about what the wallet does, what is is built with, and how to use it.

### Installing dependencies and environment configuration
* Download and Install MyCrpto to be used key mangaement and crypto wallet - https://download.mycrypto.com/
* Install Go Ethereeum Tools - https://geth.ethereum.org/downloads/

### Start the Network
    Initialize the nodes
    
    Initialize the nodes with the genesis' json file.  This step will initilize the nodes for the zbanknet network after 

