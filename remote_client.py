
#!/usr/bin/env python2

import  socket,commands,subprocess
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.1.3"
port=7890
port2=8888
s.bind(("",port2))

msg3 = s.recvfrom(20)
if "linux" in msg3[0] :
	linux()
elif "windows" in msg3[0] :
	windows()
else :
	print ("Please type Valid Server")
	
def linux() :
	for i in range(5) :
#  sending  data to  target machine 

		cmd=raw_input("Enter your Command :  ")
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

def windows():

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


