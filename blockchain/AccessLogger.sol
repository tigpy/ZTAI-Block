// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Solidity smart contract for access logging
contract AccessLogger {
    event AccessEvent(address indexed user, string action, uint256 timestamp);

    function logAccess(string memory action) public {
        emit AccessEvent(msg.sender, action, block.timestamp);
    }
}
