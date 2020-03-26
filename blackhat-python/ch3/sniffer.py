import socket
import os

# host to listen on
host = "0.0.0.0"

# create a raw socket and bind it to the public interface

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# we want the IP headers incluced in the capture

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if using windows send an IOCTL
# to set up promiscuous mode

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

#read in a single packet
print (sniffer.recvfrom(65565))

# if using windows turn off promiscuous mode

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

