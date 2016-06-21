#!/usr/bin/env python

import socket
import sys
import struct

message = "very important data"
multicast_group = ('224.3.29.71',10000)
#Create the datagram socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#set a timeout so the socket does not block indefinitely
#when trying to receive data
sock.settimeout(0.2)

#set the time to live for message to 1 so they do not go past the
#local network segment

tt1 = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,tt1)

try:
    # send data to the multicast group
    print >> sys.stderr ,'sending "%s"' %message
    sent = sock.sendto(message,multicast_group)

    # Look for response from all recipiens
    while True:
        print >> sys.stderr ,'Waiting to receive'
        try:
            data,server = sock.recvfrom(16)
        except socket.timeout:
            print >> sys.stderr,'timed out, no more response'
            break
        else:
            print >> sys.stderr,'received "%s" from %s' %(data,server)
finally:
    sock.close()


