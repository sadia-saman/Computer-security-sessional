

""" public_key,private_key = generate_RSA_key(k/2)
encrypted_key = rsa_encrypt(round_keys[0],public_key)
print(encrypted_key)

deciphered_key = rsa_decrypt(encrypted_key,private_key)
for d in deciphered_key:
    print(chr(int(d)),end="")"""

from _1705102_f2 import *


K = [16, 32, 64,128]
inputs = []

for i in range(len(K)):
    inputs.append(input("Enter plain text :"))

import time
for i in range(len(K)):
    time1 = time.time()
    public_key,private_key = generate_RSA_key(K[i]/2)
    time2 = time.time()
    key_generation_time = time2-time1
    time1 = time.time()
    plain_text = convert_to_hex(inputs[i])
    cipher_text = rsa_encrypt(plain_text,public_key)
    time2 = time.time()
    encryption_time = time2-time1

    time1 = time.time()
    plain_text = rsa_decrypt(cipher_text,private_key)
    time2 = time.time()
    decryption_time = time2-time1
    print("k = ",K[i]," == ",key_generation_time,encryption_time,decryption_time)
 