#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def token(TestContractForZooDAO, accounts):
    return TestContractForZooDAO.deploy("Test Token", "TST", 18, 1e21, [accounts[0], accounts[1], accounts[2], accounts[3]], {'from': accounts[0]})
