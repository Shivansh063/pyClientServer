#!/usr/bin/python

import socket
import time
import subprocess
import sys

#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.1.3"
port=7890



# defining list for 10 commands counter

for i in range(5) :
#  sending  data to  target machine 
    cmd=input("Enter Your Command : ")
    s.sendto(cmd,(ip,port))
    if  'exit' in  cmd  or  'close' in cmd:
        print ("closing server..")
        exit()
    else :
         server_data=s.recvfrom(500)
#   only  server  data is stored and printed
         recv_cmd=server_data[0]
         if "not recognized" in recv_cmd :
             print ("\ncommand not found..\nmake sure you are connected to WINDOWS server\n")
         else:
             print ("\n",recv_cmd,"\n")  
	
s.close() 
