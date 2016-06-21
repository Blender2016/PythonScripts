#!/usr/bin/env python

import socket
import sys
import binascii
import struct

#Create a tcp/ip socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
sock.connect(server_address)

values = (1,'ab',2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)
print 'Values =',values

try:
    # Send Data
    print >> sys.stderr,'sendibg %r' %binascii.hexlify(packed_data)
    sock.sendall(packed_data)
finally:
    print >> sys.stderr,'Closing Socket'
    sock.close()

