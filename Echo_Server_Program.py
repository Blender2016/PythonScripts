#!/usr/bin/env pyton

import socket
import sys

#create a tcp socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket to the port
server_address=('localhost',10000)
print >> sys.stderr, 'starting up on %s port %s' %server_address
sock.bind(server_address)
#listen for incoming connection
sock.listen(1)
while True:
    # Wait for a connection
    print >> sys.stderr,'Waiting for a connection'
    connectionChannel,client_address = sock.accept()
    try:
        print >> sys.stderr,'connection from',client_address
        #Receive the data in small chunks and retransmit it
        while True:
            data=connectionChannel.recv(16)
            print >>sys.stderr ,'received "%s"' %data
            if data:
                print >>sys.stderr,'sending data back to the client'
                connectionChannel.sendall(data)
            else :
                print >>sys.stderr,'no data from',client_address
                break
    finally:

        #Clean up th connection
        connectionChannel.close()



