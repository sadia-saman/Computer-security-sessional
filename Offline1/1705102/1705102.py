from numpy import integer
from _1705102_f2 import *

plain_text = input("plain text : ")
key = input("key : ")

j = 0
padding = 0x20

key_hex = []
while(j<16):
    if j< len(key) :
        key_hex.append(hex(ord(key[j])))
    else:
        key_hex.append(padding)
    j = j+1


round_keys = generate_round_key(key_hex)


i=0
while(i<len(plain_text)):
    j=i
    pt_block = []
    while(j<16):
        if j< len(plain_text) :
            pt_block.append(hex(ord(plain_text[j])))
        else:
            pt_block.append(padding)
        j = j+1


    i = i+16