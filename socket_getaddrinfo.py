#!/usr/bin/env python

import socket

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names"""
    return dict( (getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols= get_constants('IPPROTO_')
#print families
#print types
print protocols
for response in socket.getaddrinfo('www.python.org','http'):
    family ,socktype ,proto ,canonname ,sockaddr = response
    print 'Family :',families[family]
    print 'Type :',types[socktype]
    print 'Protocol :',protocols[proto]
    print 'Canonical name:', canonname
    print 'Socket address:', sockaddr


