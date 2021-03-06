#!/usr/bin/env python

import socket
import sys
import struct

multicast_group='224.3.29.71'
server_address = ('',10000)

#Create the socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# tell the operating system to add the socket to the multicast group
# on all interfaces
#
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sl',group,socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

while True:
    print 'waiting to receive message'
    data,address = sock.recvfrom(1024)
    print >> sys.stderr,'\nreceived %s bytes from %s' % (len(data),address)
    print data
    print >>sys.stderr,"sending acknowledgement to",address
    sock.sendto('ack',address)


