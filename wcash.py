from web3 import Web3, HTTPProvider
import rlp
from ethereum.transactions import Transaction
provider = HTTPProvider('https://ropsten.infura.io/v2QCDR7v7cgH6fy0y171')
web3 = Web3(provider)

tx = Transaction(
            nonce=web3.eth.getTransactionCount('0xFed55B453dBb0589ec5433a9318C09f1766D7dAb'),
            gasprice=21000,
            startgas=100000,
            to='0xa5Acc472597C1e1651270da9081Cc5a0b38258E3',
            value=12345,
            data=b'',
    )
#tx.sign('d2432061d3a6cab6a2f3f635c5dda4bb5c0b9c64285c2aa11d586402f66f0507')
#raw_tx = rlp.encode(tx)
#raw_tx_hex = web3.toHex(raw_tx)
#hash=web3.eth.sendRawTransaction(raw_tx_hex)
#print(hash)
#receipt=web3.eth.getTransactionReceipt(hash)
#print(receipt)
#print(web3.eth.getTransactionReceipt('0xd8959c67e9a06335ca770606a44bc9649b8ac468f6e278d5e547f2833c5b1ce2'))


#con=web3.eth.contract('0xd5855dcce8933cea211fed171a31f19703a3f8be')
con=web3.contract('0xd5855dcce8933cea211fed171a31f19703a3f8be')

var=con.transact().balanceOf("0xa5Acc472597C1e1651270da9081Cc5a0b38258E3")
#transfer('0xa5Acc472597C1e1651270da9081Cc5a0b38258E3', 82345)
