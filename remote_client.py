
#!/usr/bin/env python2

import  socket,commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.1.3"
port=7890
port2=8888
s.bind(("",port2))

# defining list for 10 commands counter

for i in range(5) :
#  sending  data to  target machine 

	cmd=raw_input("Enter your Message :  ")
	if cmd == 'reboot' :
		print ("   This command may disconnect with server machine ")
                continue
	else :
	      	s.sendto(cmd,(ip,port))
	if  'exit' in  cmd  or  'close' in cmd:
		print "closing server.."
		exit()
	
	data = s.recvfrom(20)
	rec_data = data[0]
	if "sh: 1" in rec_data :
		print ("     Please enter a valid command ")
	else :
		print rec_data
	

	
	
s.close()



#catch [System.Management.Automation.CommandNotFoundException] {
 # write-host 'CommandNotFoundException'
#}
