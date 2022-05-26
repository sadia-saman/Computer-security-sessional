from http.server import CGIHTTPRequestHandler
from operator import xor
import numpy as np


"""Tables"""

from BitVector import *
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

b = BitVector(hexstring="4E")
int_val = b.intValue()
s = Sbox[int_val]
s = BitVector(intVal=s, size=8)
#print(s.get_bitvector_in_hex())

AES_modulus = BitVector(bitstring='100011011')

bv1 = BitVector(hexstring="02")
bv2 = BitVector(hexstring="63")
bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
#print(bv3)



######..........................AES functions............................######

def g(word,round):
## circularbyteleftshiftof
    ret = []
    i = 0
    while i < 3:
        ret.append(word[i+1])
        i=i+1
    ret.append(word[0])


## ByteSubstitution
    i = 0
    while i < 4:
        ret[i] = Sbox[ret[i]]
        i=i+1

## adding round constant
    rconst = [round,0,0,0]
    i = 0
    while i < 4:
        ret[i] = xor(ret[i],rconst[i])
        i=i+1
    return ret
    




def generate_round_key(key):
    round_keys = [[]]
    round_keys.insert(0,key)

    rc=[0,1]
       
    r=1
    while r<11 :
        word0 = []
        word1 = []
        word2 = []
        word3 = []
        round_keys.append([])
        if r>1:
            if rc[r-1]<128:
                rc.append(rc[r-1]*2)
            else:
                rc.append(xor((rc[r-1]*2),int(0x11B)))
        i=0
        while i<4:
            word0.append(key[i])
            word1.append(key[4+i])
            word2.append(key[8+i])
            word3.append(key[12+i])
            i = i+1

        g_word3 = g(word3,rc[r])
        
        word4 = []
        word5 = []
        word6 = []
        word7 = []

        i = 0
        #print(word3,g_word3)
        while i < 4:
            word4.append(xor(word0[i],g_word3[i]))
            i=i+1
        
        i = 0
        while i < 4:
            word5.append(xor(word4[i],word1[i]))
            i=i+1

        i = 0
        while i < 4:    
            word6.append(xor(word5[i],word2[i]))
            i=i+1

        i = 0
        while i < 4:
            word7.append(xor(word6[i],word3[i]))
            i=i+1

        round_keys[r] = word4
        round_keys[r].extend(word5)
        round_keys[r].extend(word6)
        round_keys[r].extend(word7) 
        key = round_keys[r]
        r = r+1
        
    return round_keys
        

def mix_column(block):
    ret_block = [[0 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            val = 0
            for p in range(4):
                b = Mixer[r][p].gf_multiply_modular(BitVector(intVal = block[p][c]), AES_modulus, 8)
                val = xor(val,b.intValue())
            ret_block[r][c] = val
    return ret_block


def inverse_mix_column(block):
    ret_block = [[0 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            val = 0
            for p in range(4):
                b = InvMixer[r][p].gf_multiply_modular(BitVector(intVal = block[p][c]), AES_modulus, 8)
                val = xor(val,b.intValue())
            ret_block[r][c] = val
    return ret_block   



def aes_encrypt(pt_block,round_keys):
    for round in range(11):
        key_block = make_matrix_block(round_keys[round]) 

        if round>0 :
            for r in range(4):
                for c in range(4):
                    pt_block[r][c] = Sbox[pt_block[r][c]]
            

            for r in range(4):
                pt_block[r] = np.roll(pt_block[r],r*-1)

            if round<10:
                pt_block=mix_column(pt_block)
            #print_block(pt_block)

        for r in range(4):
            for c in range(4):
                pt_block[r][c] =xor(pt_block[r][c],key_block[r][c])

    return pt_block



def AES_decrypt(cipher_block,round_keys):
    for round in range(11):
        key_block = make_matrix_block(round_keys[10-round])
        #round key addition
        for r in range(4):
            for c in range(4):
                cipher_block[r][c] =xor(cipher_block[r][c],key_block[r][c])

        
        if round<10 :
            #inverse mix column
            if round>0:
                cipher_block=inverse_mix_column(cipher_block)

            #inverse shift row
            for r in range(4):
                cipher_block[r] = np.roll(cipher_block[r],r)
            
            #Inverse substitute bytes
            for r in range(4):
                for c in range(4):
                    cipher_block[r][c] = InvSbox[cipher_block[r][c]]

    
    deciphered_block = matrixToLinear(cipher_block)

    return deciphered_block
#.......................................................................

def print_block(block):
    for r in range(4):
        for c in range(4):
            print(hex(block[r][c]),end=" ")
        print()
    print()

def print_text(text):
    for t in text:
        print(chr(t),end="")
    print("   [IN ASCII]")

def print_hex(text):
    for t in text:
        print(hex(t)[2:],end="")
    print("   [IN HEX]")
        

def make_linear_block(input):
    j = 0
    padding = 32
    block = []
    while(j<16):
        if j< len(input) :
            block.append(ord(input[j]))
        else:
            block.append(padding)
        j = j+1
    return block


def make_matrix_block(input):
    mat_block = [[0 for _ in range(4)] for _ in range(4)]
    r=0
    c=0
    j=0
    while(j<16):
        mat_block[r][c]= input[j]
        j = j+1
        r = r+1
        if(r==4):
             c = c+1
             r = 0
    return mat_block


def matrixToLinear(block):
    linear_block = []
    r=0
    c=0
    j=0
    while(j<16):
        linear_block.append(block[r][c])
        j = j+1
        r = r+1
        if(r==4):
             c = c+1
             r = 0
    return linear_block



####################.........RSA functions.....................##########################

def generate_RSA_key(k):
    key1=0
    key2 =0
    low = int(2**(k-1))
    high = int(2**k)
    #print(low,high)
    while low<high:
        bv = BitVector(intVal =low)
        if bv.test_for_primality()>0:
            if key1==0:
                key1 = low
            else :
                key2 =low
                break
        low = low + 1

    if key1==0 or key2==0 :
        print("key not found",key1,key2)
    n = key1*key2
    psi = (key1-1) * (key2-1)

    low = 2
    e = 0
    while low<psi :
        if (psi%low)!=0 :
            e =low
            break
        low =low+1
    d = get_modular_inverse(e,psi)

    public_key = [e,n]
    private_key = [d,n]
    return public_key,private_key



def rsa_encrypt(block,public_key):
    for i in range(len(block)):
        block[i] = pow(block[i],public_key[0],public_key[1])
    return block



def rsa_decrypt(cipher_block,private_key):
    #print(private_key)
    for i in range(len(cipher_block)):
        cipher_block[i]= pow(cipher_block[i],private_key[0],private_key[1])
    return cipher_block


def get_modular_inverse(val,mod):
    d = pow(val, -1, mod)
    return d

def convert_to_hex(input):
    output=[]
    for i in input:
        output.append(ord(i))      
    return output  

        



    

    

