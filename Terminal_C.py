# Terminal C

import sys
sys.path.append("../Public") 
from Encryption import encrypt
from Decryption import decrypt

# class for Public Key and Private Key
class Key:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

def main():
    # Loops until user quits
    while (True):
        
        # User Prompt
        print("\n##############################")
        print("\nTerminal C")
        print("\nRead message (1)")
        print("Send message (2)")
        print("Quit (3)")
        choice = int(input("\nWhat would you like to do? "))
        
        # Reading message
        if (choice == 1):
            
            # Open the Public Channel and C's Private Key
            public_channel = open("/media/sf_CS_465_WI/RSA Project/Public/PublicChannel.txt", 'r')
            private_file = open("/media/sf_CS_465_WI/RSA Project/PC_C/PrivateKey_C.txt", 'r')
            
            # Obtain d
            readFile = private_file.readline()
            d = readFile.removeprefix(readFile[:4])
            d = d.removesuffix(d[-1:])
            d = int(d)
            
            # Obtain n
            readFile = private_file.readline()
            n = readFile.removeprefix(readFile[:4])
            n = n.removesuffix(n[-1:])
            n = int(n)
            
            # Create Private Key
            private = Key(d, n)
            
            # Decrypt message
            ciphertext = public_channel.readline()
            plaintext = decrypt(ciphertext, private)
            
            # Output to user
            print()
            print(plaintext)
            
            # Close files and prompt to continue
            public_channel.close()
            private_file.close()
            print("\nEnd of message")
            input("(Enter to continue)")
            
        # Writing message
        elif (choice == 2):
            
            # Open the Public Channel and the Public Keys
            public_channel = open("/media/sf_CS_465_WI/RSA Project/Public/PublicChannel.txt", 'w')
            public_file = open("/media/sf_CS_465_WI/RSA Project/Public/PublicKeys.txt", 'r')
            
            # User A -> Obtain e
            readFile = public_file.readline()
            e_A = readFile.removeprefix(readFile[:11])
            e_A = e_A.removesuffix(e_A[-1:])
            e_A = int(e_A)
            
            # User A -> Obtain n
            readFile = public_file.readline()
            n_A = readFile.removeprefix(readFile[:11])
            n_A = n_A.removesuffix(n_A[-1:])
            n_A = int(n_A)            
            
            # User B -> Obtain e
            readFile = public_file.readline()
            e_B = readFile.removeprefix(readFile[:11])
            e_B = e_B.removesuffix(e_B[-1:])
            e_B = int(e_B)
            
            # User B -> Obtain n
            readFile = public_file.readline()
            n_B = readFile.removeprefix(readFile[:11])
            n_B = n_B.removesuffix(n_B[-1:])
            n_B = int(n_B)           
            
            # Creating the Public Keys
            public_A = Key(e_A, n_A)
            public_B = Key(e_B, n_B)
            
            # User inputs message
            message = input("\nEnter message: ")
            
            # Asks user for recipient
            print("\nUser A (1)")
            print("User B (2)")
            choice = int(input("Who to send to? "))            
            
            # Continuous loop until user chooses valid recipient
            ciphertext = ""
            while (True):
                # recipient -> User A
                if (choice == 1):
                    ciphertext = encrypt(message, public_A)
                    break
                    
                # recipient -> User B
                elif (choice == 2):
                    ciphertext = encrypt(message, public_B)
                    break
                    
                # invalid recipient
                else:
                    print("Invalid recipient. Please try again.\n")
                    print("User A (1)")
                    print("User B (2)")
                    choice = int(input("Who to send to? "))
                    
            # Write message to the Public Channel
            public_channel.write(ciphertext)
            
            # Close files and prompt to continue
            public_channel.close()
            public_file.close()
            if (choice == 1):
                print("\nMessage sent to User A.")
            elif (choice == 2):
                print("\nMessage sent to User B.")
            input("(Enter to continue)")        
            
        # User quits
        elif (choice == 3):
            print("\nExiting Terminal C\n")
            break
        
        # Invalid user input
        else:
            print("\nInvalid option.")
            input("(Enter to continue)")
            
    return 0

main()