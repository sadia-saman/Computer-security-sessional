from numpy import integer
from _1705102_f2 import *

#plain_text = input("plain text : ")
#key = input("key : ")
plain_text = "Two One Nine Two"
key = "Thats my Kung Fu"

j = 0
padding = 32

key_hex = []
while(j<16):
    if j< len(key) :
        key_hex.append(ord(key[j]))
    else:
        key_hex.append(padding)
    j = j+1


round_keys = generate_round_key(key_hex)

i=0
while(i<len(plain_text)):
    j=i
    pt_block = []
    while(j<(i+16)):
        if j< len(plain_text) :
            pt_block.append(ord(plain_text[j]))
        else:
            pt_block.append(padding)
        j = j+1
    
    
    for idx in range(len(pt_block)):
        pt_block[idx]=xor(pt_block[idx],round_keys[0][idx])

    for idx in range(len(pt_block)):
        pt_block[idx]=Sbox[pt_block[idx]]

        print(hex(pt_block[idx]),end=" ")
    print()


    i = i+16