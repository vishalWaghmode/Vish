#Using hashlib library
from hashlib import md5
text_ = "Danish Love Cakes"
print(md5(text_.encode()).digest().hex())





#Different Answers are due to difference of initiator variables and constants used
#Without hashlib library implementation
#This Code has one to one correspondance with https://en.wikipedia.org/wiki/MD5#Algorithm psuedoco except the S constants
#-------------Globals Start ----------------------#
from math import sin , floor 
import math
S = [i for i in range(0,32)] + [i for i in range(0,32)]
const = 0xFFFFFFFF
K = [floor(abs(math.sin(i + 1)) * (2 ** 32)) & const for i in range(64)]

rotate = lambda x,n:((x << n) | (x >> (32 - n))) & const
#-------------Globals End------------------------#
    
def md5(text):
    a0,b0,c0,d0 = 0x67452301 , 0xefcdab89 , 0x98badcfe , 0x10325476
    length  = len(text)
    text = text + b'\x80' + (b'\x00' * (512 - (((len(text)+1) * 8) % 512))) +  length.to_bytes(8, 'little')
    for i in range(0, len(text), 64):
        chunk = text[i:i+64]
        M = [int.from_bytes(chunk[j:j+4], 'little') for j in range(0, 64, 4)]
        A,B,C,D = a0, b0,c0,d0
        for j in range(64):
            if 0 <= j <= 15:
                F = (B & C) | ((~B) & D)
                g = j
            elif 16 <= j <= 31:
                F = (D & B) | ((~D) & C)
                g = ((5 * j) + 1) % 16
            elif 32 <= j <= 47:
                F = B ^ C ^ D
                g = ((3 * j) + 5) % 16
            elif 48 <= j <= 63:
                F = C ^ (B | (~D))
                g = (7 * j) % 16

            F = (F + A + K[j] + M[g]) & const
            A, D, C, B = D, C, B, (B + rotate(F, S[j])) & const
        a0 = (a0 + A) & const
        b0 = (b0 + B) & const
        c0 = (c0 + C) & const
        d0 = (d0 + D) & const
    result = (a0.to_bytes(4, 'little') +
              b0.to_bytes(4, 'little') +
              c0.to_bytes(4, 'little') +
              d0.to_bytes(4, 'little'))

    return result.hex()
text = 'Cats And Dogs'.encode("utf-8")
print(md5(text))


