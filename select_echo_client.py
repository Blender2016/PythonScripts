#!/usr/bin/env python

import socket
import sys

messages = ['This is the message.',
           'It will be sent',
           'in parts']

server_address = ('localhost',10000)
# Create a TCP/IP sockets
socks = [socket.socket(socket.AF_INET,socket.SOCK_STREAM),
         socket.socket(socket.AF_INET,socket.SOCK_STREAM)]
# Connect the socket to the port where the sever is listening
print >> sys.stderr ,'connecting to %s port %s' %server_address
for s in socks:
    s.connect(server_address)
for message in messages:
    # Send messages on both sockets
    for s in socks:
        print >> sys.stderr, '%s:sending "%s"'\
                %(s.getsockname(), message)
        s.send(message)
    # Read response on poth sockets
    for s in socks:
        data = s.recv(1024)
        print >> sys.stderr,'%s: received "%s"'%\
                (s.getsockname(),data)
        if not data:
            print >> sys.stderr,'closing sockets',s.getsockname()
            s.close()



