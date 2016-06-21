#!/usr/bin/env python

import socket
import sys

def find_service_name():
    protocol_name =raw_input("Enter Protocol Name [tcp/udp]:")
    for port in sys.argv[1:]:
        service_name=socket.getservbyport(int(port),protocol_name)
        print "(%s)[%s] => %s"%(port,protocol_name,service_name)
if __name__ == '__main__':
    find_service_name()



