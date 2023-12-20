//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }
    People [] public people;
    mapping (string => uint256) public nameTonumber;

    

    function store (uint256 _favnum) public {
        favoriteNumber = _favnum;
    }

    function retrieve () public view returns (uint256) {
        return favoriteNumber;
    }

    function addPeople (string memory _name, uint256 _favnum) public {
        people.push(People(_favnum, _name));
        nameTonumber [_name] = _favnum;
    }


}
