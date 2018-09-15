#!/usr/bin/env python2

import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
#ip="192.168.1.3"
port=7890
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port))

# defining  empty list 
x=[]
for  i in range(5) :
#  now receiving data
	data=s.recvfrom(100)
	print  "only data :  ",data[0]
	x.append(data[0])

print  x
s.close()


