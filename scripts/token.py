#!/usr/bin/python3

from brownie import TestContractForZooDAO, accounts, config

initial_supply = 1e21 # 1000
token_name = "ZooDAO Token"
symbol = "ZDT"
decimals = 18

def main():
    whitelist = ['0x9Ac2Fa5e617663B9cF4E77af38bb89d02BD307c4', '0xd7067E6AcC2B703df74b7c83464c4dfB2Ee27d43', '0x84c59FeC3a0022d37eB56dfA6b8e98AC24853732', '0xf3A4668E43258c98B60313a5de7604Fb0A7416A5']
    account = accounts.add(config["wallets"]["from_key"])

    overrides = {
        'from': account
    }

    return TestContractForZooDAO.deploy(
        token_name, 
        symbol, 
        decimals, 
        initial_supply, 
        whitelist, 
        overrides, 
        publish_source=True
    )
