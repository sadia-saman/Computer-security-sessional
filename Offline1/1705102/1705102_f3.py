
##....Independent implementation of AES



from _1705102_f2 import *
from time import *

plain_text = input("plain text : ")
key = input("key : ")
""" plain_text = "Two One Nine Two"
key = "Thats my Kung Fu" """


#.. round key generation
key_hex = make_linear_block(key)
start = time()
round_keys = generate_round_key(key_hex)
key_generation_time=time()-start 

i=0
encryption_time = 0
cipher_text = []
while(i<len(plain_text)):
    if(len(plain_text[i:])<16):
        block = make_linear_block(plain_text[i:])
    else:
        block = make_linear_block(plain_text[i:i+16])
    i = i+16
    pt_block = make_matrix_block(block)
    start = time()
    cipher_block = aes_encrypt(pt_block,round_keys)
    encryption_time = encryption_time + (time() - start)
    cipher_text.extend(matrixToLinear(cipher_block))

print("\nCiphered text : ")
print_hex(cipher_text)
print_text(cipher_text)

deciphered_text = []
i=0

decryption_time =0
while i<len(cipher_text):
    start =time()
    deciphered_text.extend(AES_decrypt(make_matrix_block(cipher_text[i:i+16]),round_keys))
    decryption_time = decryption_time + (time()-start)
    i= i +16

print("\nDeciphered text : ")
print_hex(deciphered_text)
print_text(deciphered_text)

print("\nExecution time :")
print("Key expansion time : ",key_generation_time," seconds")
print("Encryption time : ",encryption_time," seconds")
print("Decryption time : ",decryption_time," seconds")