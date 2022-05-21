#!/usr/bin/python3
import brownie

null_address = '0x0000000000000000000000000000000000000000'

def test_sender_balance_decreases(accounts, token):
    sender_balance = token.balanceOf(accounts[0])
    amount = sender_balance // 4

    token.burn(accounts[0], amount, {'from': accounts[0]})

    assert token.balanceOf(accounts[0]) == sender_balance - amount


def test_burn_full_balance(accounts, token):
    sender_balance = token.balanceOf(accounts[0])
    amount = sender_balance

    token.burn(accounts[0], amount, {'from': accounts[0]})

    assert token.balanceOf(accounts[0]) == 0
    

def test_total_supply_affected(accounts, token):
    total_supply = token.totalSupply()
    amount = token.balanceOf(accounts[0])

    token.burn(accounts[0], amount, {'from': accounts[0]})

    assert token.totalSupply() == total_supply - amount


def test_burn_zero_tokens(accounts, token):
    sender_balance = token.balanceOf(accounts[0])

    token.burn(accounts[0], 0, {'from': accounts[0]})

    assert token.balanceOf(accounts[0]) == sender_balance


def test_insufficient_balance(accounts, token):
    balance = token.balanceOf(accounts[0])

    with brownie.reverts():
        token.burn(accounts[0], balance + 1, {'from': accounts[0]})


def test_transfer_event_fires(accounts, token):
    amount = token.balanceOf(accounts[0])

    tx = token.burn(accounts[0], amount, {'from': accounts[0]})

    assert len(tx.events) == 1
    assert tx.events["Transfer"].values() == [accounts[0], null_address, amount]


def test_cant_burn_from_someone_elses_address(accounts, token):
    amount = token.balanceOf(accounts[1])

    with brownie.reverts():
        token.burn(accounts[1], amount, {'from': accounts[0]})

