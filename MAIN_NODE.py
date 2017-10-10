from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from time import sleep
# Code provided for test purpose by Mchain Team 
import socket
import sys
import os



web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))
ERROR="ERROR"

# Create a TCP/IP socket
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address_2 = ('0.0.0.0', 10001)
#print >>sys.stderr, 'starting up on %s port %s' % server_address_2
sk=sock_server.bind(server_address_2)
#Listen for incoming c


#if sock_server:
print("************************************************")
print(" SERVER STARTED")
print("*************************************************")
sock_server.listen(1)

#try:
#****************************Connect to Pi Display*******************
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('192.168.1.6', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#******************************************************************
def payment(str):
	unlock=web3.personal.unlockAccount(web3.eth.accounts[0],"badrafaf123",3600)

	if unlock:
		print("************************************************")
		print ("Account unlocked successfully")
		print("************************************************")
		tras_hash=web3.eth.sendTransaction({'from': web3.eth.accounts[0], 'to': web3.eth.accounts[1],'value': web3.toWei(0.000001, "ether"),'data':web3.toHex('EHTP/INPT')})
		print (tras_hash)
		sock.sendall("ID:"+tras_hash)
		print("please check : https://ropsten.etherscan.io/tx/"+tras_hash)
#	wait_status=wait_for_transaction(web3, txn_hash)
		if tras_hash:
#	    animation = "|/-\\"
#            idx = 0
		    	os.system("play processing.mp3 >/dev/null 2>&1")
		while True:
#                print animation[idx % len(animation)] + "\r",
			txn_receipt = web3.eth.getTransactionReceipt(tras_hash)
			if txn_receipt is not None:
				print("The Transaction has been included in the blokchchain")
				break
#                idx += 1
			sleep(2)
#                print animation[idx % len(animation)] + "\r",

	else:
#	print "Message ", ERROR
		print ("Error Account is locked")
	#print("************************************************")
	if txn_receipt:
		print("************************************************")
		print ("transaction informations:")
		print (txn_receipt)
		print("************************************************")
		sock.sendall("Transaction Confirmed")
		os.system("play transaction_has_been_confirmed.mp3 >/dev/null 2>&1")
	return

#-----------------------------------------------
while True:
    # Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock_server.accept()
	try:
		print >>sys.stderr, 'connection from', client_address
		connection.sendall("ok")

        # Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(16)
			print >>sys.stderr, 'received "%s"' % data
			if data:
				print >>sys.stderr, 'sending data back to the client'
				payment(data) 
#      connection.sendall(data)
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
	finally:
        # Clean up the connection
		connection.close()









#*****************************Server exception*****************************
#finally:
#print >>sys.stderr, 'closing socket'
#sock.close()

