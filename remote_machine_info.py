#!/usr/bin/env python

import socket
import sys

def get_remote_machine_info():

    host_num= len(sys.argv)
    host_list= sys.argv

    for remote_host_name in host_list[1:]:
        try:
            ip_address=socket.gethostbyname(remote_host_name)
            print " %s [IP] : %s" %(remote_host_name,ip_address)
        except socket.error ,err_msg:
            print "%s : %s" %(remote_host_name,err_msg)

if __name__ == '__main__':
    get_remote_machine_info()

