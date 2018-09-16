#!/usr/bin/env python2

import  socket
import time
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="127.0.0.1"
port=7890
port2=9999
#  bind ip and port with bind function that takes input as tuple
s.bind(("",port))

# defining  empty list 
x=[]
username = s.recvfrom(20)
password1 = s.recvfrom(20)
ipcheck = username[1]
ipcheck2 = password1[1]

if username[0] == 'root' and password1[0] == '123' :
	s.sendto("ok",(ip,port2))
	while 4 > 2 :
#  now receiving data
		data=s.recvfrom(100)
		data2 = data[1]
		if ipcheck[0] == ipcheck1[0] and data2[0] == ipcheck1[0] :
			print  "only data :  ",data[0]
			x.append(data[0])
			x = data[1]
			print x[0]
		else :
			print ("   3rd Machine Interuption  ")
			continue 
else :
	print ("Enter Valid details")

s.close()
