
##........Alice [sender]


from _1705102_f2 import *

""" plain_text = input("plain text : ")
key = input("key : ") """
plain_text = "Two One Nine Two"
key = "Thats my Kung Fu" 

#.. round key generation
key_hex = make_linear_block(key) 
round_keys = generate_round_key(key_hex)

#...encryption........
i=0
cipher_text = []
while(i<len(plain_text)):
    if(len(plain_text[i:])<16):
        block = make_linear_block(plain_text[i:])
    else:
        block = make_linear_block(plain_text[i:i+16])
    i = i+16  
    cipher_block = aes_encrypt(make_matrix_block(block),round_keys) 
    cipher_text.extend(matrixToLinear(cipher_block))

public_key,private_key = generate_RSA_key(32)
encrypted_key = rsa_encrypt(round_keys[0],public_key)


import os
import pathlib

directory = "Don't Open this"
parent_dir  = os.getcwd() 
new_dir = pathlib.Path(parent_dir, directory)
new_dir.mkdir(parents=True, exist_ok=True) 


str_ = ""+str(private_key[0])+" "+str(private_key[1])
new_file = new_dir / 'keyfile.txt'
new_file.write_text(str_)
new_file = new_dir / 'textfile.txt'
new_file.write_text("")

#print(cipher_text,encrypted_key)



import socket			

s = socket.socket()		
print ("Socket successfully created")
port = 12345			

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")	 

while True:
    c, addr = s.accept()	
    print ('Got connection from', addr )

    #sending cipher text
    c.send(len(cipher_text).to_bytes(1024,'little'))
    for t in cipher_text:
        c.send(int(t).to_bytes(1024,'little'))

    #sending encrypted key
    c.send(len(encrypted_key).to_bytes(1024,'little'))
    for k in encrypted_key:
        c.send(int(k).to_bytes(1024,'little'))
    
    c.close()
    break


#file = open(parent_dir+'/'+directory+'/textfile.txt','r')

while True:
    text =  new_file.read_text()
    if len(text)>0 :
        break
    

if text==plain_text:
    print("Encryption successful.")
else:
    print(text)
    print("Encryption failed.")




