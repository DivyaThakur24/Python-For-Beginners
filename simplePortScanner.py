# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:13:03 2022

@author: divya
"""

#import socket
#
#for port in range(20,30):
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    result = sock.connect_ex(("192.168.0.250", port))
#    if result == 0:
#        print("Port " + str(port) + " is open")
#    else:
#        print("Port " + str(port) +  " is closed")
#    sock.close()

#!/usr/bin/python3

import socket
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port(s) you want to scan: "))

for port in range(port,port+10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    
    def portScanner(port):
        if s.connect_ex((host, port)):
            print("The port", port," is closed")
        else:
            print("The port", port, " is open")

    portScanner(port)
    