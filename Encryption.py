# Encryption

import sys

# class for Public Key and Private Key
class Key:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Generates the Public Key and the Private Key
# output: public key, private key
# 
def generateKeys():
    
    # Step 1: Choose two prime numbers
    p, v = 17, 11
    
    # Step 2: Multiply prime numbers
    n = p * v
    
    # Step 3: Euler's number
    euler = (p - 1) * (v - 1)
    
    # Step 4: Choose number relatively prime to Euler's number
    e = 7
    
    # Step 5: Calculate d
    d = 0 #Need Euclidean Algorithm
    
    # Step 6: Finalize Public Key and Private Key
    public = Key(e, n)
    private = Key(d, n)
    
    return public, private

# Converts a string to an array of ASCII code
# input: string to be converted
# output: array of each letter of string converted to ASCII code
#
def convertToAscii(inputString):
    ascii_code = []
    for i in range(len(inputString)):
        x = str(ord(inputString[i]))
        if (ord(inputString[i]) < 100):
            x = "0" + x
        ascii_code.append(x)
            
    return ascii_code

# Main function for Encryption
# input: message in plaintext, public key
# output: ciphertext
#
def encrypt(plaintext, public):
    
    # Step 1: Convert plaintext into ASCII code
    ascii_array = convertToAscii(plaintext)
    
    # Step 2: Create blocks of ASCII code
    #blocks_array = []
    #i = 0
    #while (i < len(ascii_array)):
    #    if (i+1 >= len(ascii_array)):
    #        x = int(ascii_array[i] + "032")
    #        blocks_array.append(x)
    #    else:
    #        x = int(ascii_array[i] + ascii_array[i+1])
    #        blocks_array.append(x)
    #    i += 2
    
    # Step 3: Mod operator with e from Public Key
    modulus_array = []
    i = 0
    for i in range(len(ascii_array)):
        x = (int(ascii_array[i]) ** public.num1) % public.num2
        modulus_array.append(str(x))
        
    # Step 4: Breakup the blocks
    #breakup_array = []
    #i = 0
    #for i in range(len(modulus_array)):
    #    value = modulus_array[i]
    #    first_digits = value[:-3]
    #    last_3_digits = value[-3:]
    #    if (len(value) > 3):
    #        breakup_array.append(first_digits)
    #    breakup_array.append(last_3_digits)
        
    # Step 5: Create Ciphertext string
    ciphertext = ""
    i = 0
    for i in range(len(modulus_array)):
        character = chr(int(modulus_array[i]))
        ciphertext += character
    
    # Demonstration purposes
    #print("\nPlaintext:", plaintext)
    #print("ASCII:", ascii_array)        # Step 1
    #DO NOT USE print("Blocks:", blocks_array)      # Step 2
    #print("Modulus:", modulus_array)    # Step 3
    #DO NOT USE print("Breakup:", breakup_array)    # Step 4
    #print("Ciphertext:", ciphertext)    # Step 5
    
    return ciphertext

# Used for testing purposes
def main():
    
    
    
    return 0
