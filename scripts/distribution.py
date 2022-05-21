#!/usr/bin/python3

from brownie import TestContractForZooDAO, accounts, config
import math

initial_supply = 1000
decimals = 18

def main():
    token = TestContractForZooDAO.at('0x760108d471f483d2A843C8C086bd431D4cF7ab1b')

    whitelist = [
        '0xd7067E6AcC2B703df74b7c83464c4dfB2Ee27d43', 
        '0x84c59FeC3a0022d37eB56dfA6b8e98AC24853732', 
        '0xf3A4668E43258c98B60313a5de7604Fb0A7416A5', 
        '0x5B3C2584364B0C153C2e0Ca52EfE8F8699deC3Df'
    ]
    
    account = accounts.add(config["wallets"]["from_key"])

    overrides = {
        'from': account
    }

    amount = math.floor(1000 / len(whitelist)) * 10 ** decimals

    for i in range(0, len(whitelist)):
        token.transfer(whitelist[i], amount, overrides)
