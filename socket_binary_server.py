#!/usr/bin/env python

import socket
import sys
import struct
import binascii

#Create a tcp/ip socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
    print >> sys.stderr,'\nwaiting for a connection'
    connection,client_address=sock.accept()
    try:
        data=connection.recv(unpacker.size)
        print >> sys.stderr,'received %r ' %binascii.hexlify(data)
        unpacked_data=unpacker.unpack(data)
        print >>sys.stderr,'unpacked :',unpacked_data
    finally:
        connection.close()
