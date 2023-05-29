#This code requires python 3.8+ 
from math import gcd
def encrypt(public_key:int,n:int,input_:str)->str:
    return [(ord(char)**public_key)%n for char in input_]
def decrypt(private_key:int,n:int,input_:list)->str:
    return [chr(((num)**private_key)%n) for num in input_]
    
p = 31#any Prime
q = 97#any Prime
n = p * q
phi = (p-1) * (q - 1)
public = [i for i in range(phi) if gcd(i, phi) == 1][0] #Can replace with any number where gcd(phi,select number) ==  1
private = pow(public, -1, phi)#power support multiplicative inverse since python 3.8+
input_ = "Sixth Here"
enc = encrypt(public,n,input_)
dec = decrypt(private,n,enc)
print("Encrypted text =>","".join(map(str,enc)))
print("Decrypted text =>","".join(dec))
