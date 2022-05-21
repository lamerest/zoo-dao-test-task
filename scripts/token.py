#!/usr/bin/python3

from brownie import TestContractForZooDAO, accounts, config

initial_supply = 1e21 # 1000
token_name = "ZooDAO Token"
symbol = "ZDT"
decimals = 18

def main():
    account = accounts.add(config["wallets"]["from_key"])

    overrides = {
        'from': account
    }

    return TestContractForZooDAO.deploy(
        token_name, 
        symbol, 
        decimals, 
        initial_supply, 
        overrides, 
        publish_source=True
    )
