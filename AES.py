#Run pip install pycryptodome to install necessary packages
#This implementation uses continuous block cipher
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext, key):
    init = get_random_bytes(AES.block_size)#For CBC mode generates init combination
    cipher = AES.new(key, AES.MODE_CBC, init)
    ciphertext = cipher.encrypt(plaintext)
    return init + ciphertext #adds initial combination to 

def decrypt(ciphertext, key):
    init = ciphertext[:AES.block_size]#gets initial combination to reverse
    cipher = AES.new(key, AES.MODE_CBC, init)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext

key = b'aaaaaaaaaaaaaaaa'#16, 24, or 32 length strings
plaintext = b'Olivia loves fish'
ciphertext = encrypt(pad(plaintext,16), key)
print("Encrypted:", ciphertext)
decrypted = unpad(decrypt(ciphertext, key),16)
print("Decrypted:", decrypted)
