# Chapter 2 of Black hat Python
# Code has been fixed to work with
# Python 3 and interact with tcp_server script

import socket

target_host = "localhost"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send data
client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response)  
