# Decryption

import sys
#from Encryption import encrypt

# class for Public Key and Private Key
class Key:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Converts an array of ASCII code into a string
# input: array of ASCII code
# output: string converted from ASCII code
#
def convertToString(inputArray):
    outputString = ""
    for i in inputArray:
        outputString += chr(i)
    return outputString

# Main function for Decryption
# input: message in ciphertext, private key
# output: plaintext
#
def decrypt(ciphertext, private):
    
    # Step 1: Convert ciphertext string into array of ASCII code
    cipher_array = []
    i = 0
    for i in range(len(ciphertext)):
        cipher_array.append(str(ord(ciphertext[i])))
    
    # Step 2: Mod operator with d from Private Key
    reverseMod_array = []
    i = 0
    for i in range(len(cipher_array)):
        x = (int(cipher_array[i]) ** private.num1) % private.num2
        reverseMod_array.append(x)
        
    # Step 3: Convert ASCII code into plaintext
    plaintext = ""
    plaintext = convertToString(reverseMod_array)
    
    # Demonstration purposes
    #print("Ciphertext:", ciphertext)
    #print("ASCII Array:", cipher_array)
    #print("Reverse Modulus:", reverseMod_array)
    #print("Message:", plaintext)
    
    return plaintext

# Used for testing purposes
def main():
    
    
    
    return 0
