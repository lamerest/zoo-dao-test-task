// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract TestContractForZooDAO is ERC20 {
	constructor(
		string memory _name,
		string memory _symbol,
		uint256 _decimals,
		uint256 _totalSupply
	) public ERC20(_name, _symbol) {
		_mint(msg.sender, _totalSupply);
	}

	function burn(address account, uint256 amount) public {
		require(msg.sender == account, 'You can`t burn not your funds');

		_burn(account, amount);
	}
}
