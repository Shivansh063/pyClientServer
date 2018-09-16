
#!/usr/bin/env python2

import  socket
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="127.0.0.1"
port=7890
port2=9999

s.bind(("",port2))

user_name = raw_input("Enter Username :  ")
s.sendto(user_name,(ip,port))
password = raw_input("Enter Password :  ")
s.sendto(password,(ip,port))
check1 = s.recvfrom(200)
if check1[0] == "ok" : 
	while 4 > 2 :
#  sending  data to  target machine 
		msg=raw_input("enter your message :   ")
		s.sendto(msg,(ip,port))
else : 
	print ("Please Fill Correct Details ...")



























































