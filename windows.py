#!/usr/bin/env python2

import  socket,commands,subprocess
import time
from subprocess import PIPE
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.43.139"
port=7890
port2=8888
s.bind(("",port2))

for i in range(5) :
	msg = raw_input("Enter Your Command : ")
	s.sendto(msg,(ip,port))
	
	if 'exit' in msg or 'close' in msg :
		print ("Closing Server ...")
		time.sleep(2)
		exit()
	recvdata = s.recvfrom(50000)
	recdata = recvdata[0]

	if "not recognized" in recdata :
		print ("Please Enter Valid Command")
	else : 
		print ("\n",recdata,"\n")



	
