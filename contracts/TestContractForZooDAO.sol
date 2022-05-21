// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract TestContractForZooDAO is ERC20 {
	constructor(
		string memory _name,
		string memory _symbol,
		uint256 _decimals,
		uint256 _totalSupply,
		address[] memory whitelist
	) public ERC20(_name, _symbol) {
		for (uint256 i = 0; i < whitelist.length; i++) {
			_mint(whitelist[i], _totalSupply / whitelist.length);
		}

		uint256 leftToMint = _totalSupply - totalSupply();

		if (leftToMint > 0) {
			_mint(msg.sender, leftToMint);
		}
	}

	function burn(address account, uint256 amount) public {
		_burn(account, amount);
	}
}
