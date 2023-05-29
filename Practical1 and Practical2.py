# Practical1
input_: str = input("Give Input String ")
print("Some of the values are not visible as Garbage is Outputed")
print("Xor=>" + "".join([chr(ord(char) ^ 127) for char in input_]))
print("And=>" + "".join([chr(ord(char) & 127) for char in input_]))
print("Or=>" + "".join([chr(ord(char) | 127) for char in input_]))

# Practical2
import math


def Encrypt(key: int, string: str) -> str:
    matrix = [["_" for i in range(key)] for j in range(math.ceil(len(string) / key))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (key * i + j) >= len(string):
                break
            matrix[i][j] = string[(key * i + j)]
    return "".join(
        [
            "".join(i)
            for i in [
                [matrix[i][j] for i in range(len(matrix))]
                for j in range(len(matrix[0]))
            ]
        ]
    )
def Decrypt(key: int, string: str) -> str:
    matrix = [["_" for i in range(key)] for j in range(math.ceil(len(string) / key))]
    index = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if index >= len(string):
                break
            matrix[i][j] = string[index]
            index += 1

    return "".join(["".join(i) for i in matrix])

Key_Size: int = int(input("Give Key Size "))
encrypting_String: str = input("Give Encrypting String ")
print("Encrypted String=> ",Encrypt(Key_Size,encrypting_String).replace("_",""))
print("Decrypted String=> ",Decrypt(Key_Size,Encrypt(Key_Size, encrypting_String)).replace("_",""))
