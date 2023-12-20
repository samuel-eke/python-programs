from solcx import compile_standard, install_solc
import json

with open ('.\simplestorage.sol', 'r') as file:
    simple_storage_file = file.read()

#compiling in python
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simplestorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", 'metadata', 'evm.bytecode', 'evm.sourceMap']}
            }
        },
    },
    solc_version="0.6.0",
)

#this line allows us to put the abi into a json file
with open ("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

#get bytecode
bytecode = compiled_sol ["contracts"]["SimpleStorage.sol"]["simplestorage"]["evm"]["bytecode"]
["object"]

#get abi
abi = compiled_sol["contracts"]["simplestorage.sol"]["simplestorage"]["abi"]