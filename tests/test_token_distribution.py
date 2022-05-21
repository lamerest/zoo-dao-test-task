#!/usr/bin/python3
import brownie, math

initial_supply = 1e21 # 1000
token_name = "ZooDAO Token"
symbol = "ZDT"
decimals = 18

def test_equal_distribution(accounts, token):
    for i in range(0, 4):
        assert token.balanceOf(accounts[i]) == token.totalSupply() // 4


def test_unequal_supply_distribution(accounts, TestContractForZooDAO):
    whitelist = [accounts[0], accounts[1], accounts[2]]
    
    distributedToken = TestContractForZooDAO.deploy(token_name, symbol, decimals, initial_supply, whitelist, {'from': accounts[0]})

    assert distributedToken.balanceOf(accounts[0]) == 333333333333333333334

    for i in range(1, 3):
        assert distributedToken.balanceOf(accounts[i]) == 333333333333333333333


def test_unequal_supply_distribution_between_6_accounts(accounts, TestContractForZooDAO):
    whitelist = [accounts[0], accounts[1], accounts[2], accounts[3], accounts[4], accounts[5]]
    
    distributedToken = TestContractForZooDAO.deploy(token_name, symbol, decimals, initial_supply, whitelist, {'from': accounts[0]})

    assert distributedToken.balanceOf(accounts[0]) == 166666666666666666670

    for i in range(1, 6):
        assert distributedToken.balanceOf(accounts[i]) == 166666666666666666666
