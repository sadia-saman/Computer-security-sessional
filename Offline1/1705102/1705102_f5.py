#........Bob [receiver]
import socket	
from _1705102_f2 import *
import os

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


#print(text,key)
s.close()


directory = "Don't Open this"
parent_dir  = os.getcwd() 
new_dir = os.path.join(parent_dir, directory)
file = new_dir + '/keyfile.txt'

check = False
while check==False :
    check = os.path.exists(file)
    print(file,check)


my_file = open(file, 'r') 
str_ = my_file.readline()
my_file.close()
print(str_)
msg = str_.split(" ")
if len(msg)==2 :
    d = int(msg[0])
    n = int(msg[1])
    deciphered_key = rsa_decrypt(key,[d,n])
    round_keys = generate_round_key(deciphered_key)
    i=0
    deciphered_text = []
    while i<len(text): 
        deciphered_text.extend(AES_decrypt(make_matrix_block(text[i:i+16]),round_keys))
        i= i +16
    file = new_dir + '/textfile.txt'
    my_file=  open(file, 'w')
    for t in deciphered_text:
        my_file.write(chr(t))
    my_file.close()
    
else:
    print("key not found")
	
