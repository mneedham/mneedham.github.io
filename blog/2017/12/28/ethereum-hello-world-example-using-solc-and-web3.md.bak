+++
draft = false
date="2017-12-28 11:03:56"
title="Ethereum Hello World Example using solc and web3"
tag=['ethereum', 'blockchain', 'smart-contracts']
category=['Ethereum']
description="Learn how to code a Hello World example on the Ethereum blockchain using solc, the Solidity smart contract language, and the web3 client library."
+++

<p>
I've been trying to find an Ethereum Hello World example and came across Thomas Conté's excellent post that shows how to <a href="http://hypernephelist.com/2016/12/13/compile-deploy-ethereum-smart-contract-web3-solc.html">compile and deploy an Ethereum smart contract with solc and web3</a>.
</p>


<p>
In the latest version of web3 the API has changed to be based on promises so I decided to translate Thomas' example. 
</p>


<p>Let's get started.</p>



<h2>Install npm libraries</h2>

<p>
We need to install these libraries before we start:
</p>



~~~bash

npm install web3
npm install abi-decoder
npm install ethereumjs-testrpc
~~~

<p>What do these libraries do?</p>


<ul>

<li>
<cite>web3</cite> is a client library for interacting with an Ethereum blockchain
</li>

<li>
<cite>abi-decoder</cite> is used to decode the hash of a smart contract so that we can work out what was in it.
</li>

<li>
<cite>ethereum-testrpc</cite> lets us spin up a local test version of Ethereum
</li>

</ul>


<h2>Smart contract</h2>

<p>
We'll still use the same smart contract as Thomas did. <cite>Token.sol</cite> is a smart contract written in the <a href="https://solidity.readthedocs.io/en/develop/">Solidity</a> language and describes money being transferred between addresses:
</p>


<p><cite>contracts/Token.sol</cite></p>



~~~text

pragma solidity ^0.4.0;

contract Token {
    mapping (address => uint) public balances;
  
    function Token() {
        balances[msg.sender] = 1000000;
    }

    function transfer(address _to, uint _amount) {
        if (balances[msg.sender] < _amount) {
            throw;
        }

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
    }
}
~~~ 

<p>
Whenever somebody tries to transfer some money we'll put 1,000,000 in their account and then transfer the appropriate amount, assuming there's enough money in the account.
</p>


<h2>Start local Ethereum node</h2>

<p>
Let's start a local Ethereum node. We'll reduce the gas price - the amount you 'pay' to execute a transaction - so we don't run out. 
</p>



~~~bash

$ ./node_modules/.bin/testrpc --gasPrice 20000
EthereumJS TestRPC v6.0.3 (ganache-core: 2.0.2)

Listening on localhost:8545
~~~

<h2>Pre requisites</h2>

<p>
We need to load a few Node.js modules:
</p>



~~~javascript

const fs = require("fs"),
      abiDecoder = require('abi-decoder'),
      Web3 = require('web3'),
      solc = require('solc');
~~~

<h2>Compile smart contract</h2>

<p>
Next we'll compile our smart contract:
</p>



~~~javascript

const input = fs.readFileSync('contracts/Token.sol');
const output = solc.compile(input.toString(), 1);
const bytecode = output.contracts[':Token'].bytecode;
const abi = JSON.parse(output.contracts[':Token'].interface);
~~~

<h2>Connect to Ethereum and create contract object</h2>

<p>Now that we've got the <a href="https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI">ABI</a> (Application Binary Interface) we'll connect to our local Ethereum node and create a contract object based on the ABI:
</p>
 


~~~javascript

let provider = new Web3.providers.HttpProvider("http://localhost:8545");
const web3 = new Web3(provider);
let Voting = new web3.eth.Contract(abi);
~~~

<h2>Add ABI to decoder</h2>

<p>
Before we interact with the blockchain we'll first add the ABI to our ABI decoder to use later:
</p>



~~~javascript

abiDecoder.addABI(abi);
~~~

<h2>Find (dummy) Ethereum accounts</h2>

<p>
Now we're ready to create some transactions! We'll need some Ethereum accounts to play with and if we call <a href="https://web3js.readthedocs.io/en/1.0/web3-eth.html#getaccounts">web3.eth.getAccounts</a> we can get a collection of accounts that the node controls. Since our node is a test one these are all dummy accounts.
</p>




~~~javascript

web3.eth.getAccounts().then(accounts => {
  accounts.forEach(account => {
    console.log(account)
  })
});
~~~


~~~text

0xefeaE7B180c7Af4Dfd23207422071599c7dfd2f7
0x3a54BaAFDe6747531a28491FDD2F36Cb61c83663
0x367e1ac67b9a85E438C7fab7648964E5ed12061e
0xB34ECD20Be6eC99e8e9fAF641A343BAc826FFFf1
0xE65587a2951873efE3325793D5729Ef91b15d5b5
0xdA232aEe954a31179E2F5b40E6efbEa27bB89c87
0x7119fEbab069d440747589b0f1fCDDBAdBDd105d
0xCacB2b61dE0Ca12Fd6FECe230d2f956c8Cdfed34
0x4F33BF93612D1B89C8C8872D4Af30Fa2A9CbfaAf
0xA1Ebc0D19dB41A96B5278720F47C2B6Ab2506ccF
~~~

<h2>Transfer money between accounts</h2>

<p>Now that we have some accounts let's transfer some money between them.</p>




~~~javascript

var allAccounts;
web3.eth.getAccounts().then(accounts => {
  allAccounts = accounts;
  Voting.deploy({data: bytecode}).send({
    from: accounts[0],
    gas: 1500000,
    gasPrice: '30000000000000'
  }).on('receipt', receipt => {
    Voting.options.address = receipt.contractAddress;
    Voting.methods.transfer(accounts[1], 10).send({from: accounts[0]}).then(transaction => {
      console.log("Transfer lodged. Transaction ID: " + transaction.transactionHash);
      let blockHash = transaction.blockHash
      return web3.eth.getBlock(blockHash, true);
    }).then(block => {
      block.transactions.forEach(transaction => {
        console.log(abiDecoder.decodeMethod(transaction.input));
      });

      allAccounts.forEach(account => {
          Voting.methods.balances(account).call({from: allAccounts[0]}).then(amount => {
            console.log(account + ": " + amount);
          });
      });
    });
  });
});
~~~

<p>Let's run in:</p>



~~~text

Transfer lodged. Transaction ID: 0x699cbe40121d6c2da7b36a107cd5f28b35a71aff2a0d584f8e734b10f4c49de4

{ name: 'transfer',
  params: 
   [ { name: '_to',
       value: '0xeb25dbd0931386eeab267981626ae3908d598404',
       type: 'address' },
     { name: '_amount', value: '10', type: 'uint256' } ] }

0x084181d6fDe8bA802Ee85396aB1d25Ddf1d7D061: 999990
0xEb25dbD0931386eEaB267981626AE3908D598404: 10
0x7deB2487E6Ac40f85fB8f5A3bC6896391bf2570F: 0
0xA15ad4371B62afECE5a7A70457F82A30530630a3: 0
0x64644f3B6B95e81A385c8114DF81663C39084C6a: 0
0xBB68FF2935080c807D5A534b1fc481Aa3fafF1C0: 0
0x38d4A3d635B451Cb006d63ce542950C067D47F58: 0
0x7878bA9138361A08522418BD1c8376Af7220a506: 0
0xf400c0e749Fe02E7073E08d713E0A207dc91FBeb: 0
0x7070d1712a25eb7FCf78A549F17705AA66B0aD47: 0
~~~

<p>
This code:</p

<ul>

<li>
Deploys our smart contract to the blockchain
</li>

<li>
Transfers £10 from account 1 to account 2
</li>

<li>
Decodes that transaction and shows the output
</li>

<li>
Show the balances of all the dummy accounts
</li>

</ul>

<p>The <a href="https://github.com/mneedham/ethereum-nursery/blob/master/eth_solc.js">full example is available</a> in my <a href="https://github.com/mneedham/ethereum-nursery">ethereum-nursery</a> GitHub repository. Thomas also has <a href="http://hypernephelist.com/2017/01/19/deploy-ethereum-smart-contract-using-client-signature.html">a follow up post</a> that shows how to deploy a contract on a remote node where client side signatures become necessary.
</p>

