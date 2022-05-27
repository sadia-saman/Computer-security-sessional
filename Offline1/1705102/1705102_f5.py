#........Bob [receiver]
import socket	
from _1705102_f2 import *

s = socket.socket()		

port = 12345			
s.connect(('127.0.0.1', port))
text = []
key = []


msg_len = int.from_bytes(s.recv(1024),'little')
for i in range(int(msg_len)):
    byte_val = s.recv(1024)
    text.append(int.from_bytes(byte_val,'little'))


msg_len = int.from_bytes(s.recv(1024),'little')
for i in range(int(msg_len)):
    byte_val = s.recv(1024)
    key.append(int.from_bytes(byte_val,'little'))


print(text,key)
s.close()

while(true)

deciphered_key = rsa_decrypt(key)
	
