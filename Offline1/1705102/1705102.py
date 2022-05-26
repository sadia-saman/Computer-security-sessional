from _1705102_f2 import *

#plain_text = input("plain text : ")
#key = input("key : ")
plain_text = "Two One Nine Two"
key = "Thats my Kung Fu"

#for rsa key k = 163264128

k =32


key_hex = make_linear_block(key)
round_keys = generate_round_key(key_hex)

i=0
cipher_text = []
while(i<len(plain_text)):
    block = make_linear_block(plain_text[i:i+16])
    i = i+16
    pt_block = make_matrix_block(block)
    cipher_block = aes_encrypt(pt_block,round_keys)
    cipher_text.extend(matrixToLinear(cipher_block))

public_key,private_key = generate_RSA_key(k/2)
encrypted_key = rsa_encrypt(round_keys[0],public_key)

deciphered_text =AES_decrypt(cipher_text,round_keys)
deciphered_key = rsa_decrypt(encrypted_key,private_key)

print(deciphered_text)
print(deciphered_key)
