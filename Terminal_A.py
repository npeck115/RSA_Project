# Terminal A

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
        print("\nTerminal A")
        print("\nRead message (1)")
        print("Send message (2)")
        print("Quit (3)")
        choice = int(input("\nWhat would you like to do? "))
        
        # Reading message
        if (choice == 1):
            
            # Open the Public Channel and A's Private Key
            public_channel = open("/media/sf_CS_465_WI/RSA Project/Public/PublicChannel.txt", 'r')
            private_file = open("/media/sf_CS_465_WI/RSA Project/PC_A/PrivateKey_A.txt", 'r')
            
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
            
            # Skipping User A's Public Key
            readFile = public_file.readline()
            readFile = public_file.readline()
            
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
            
            # User C -> Obtain e
            readFile = public_file.readline()
            e_C = readFile.removeprefix(readFile[:11])
            e_C = e_C.removesuffix(e_C[-1:])
            e_C = int(e_C)     
            
            # User C -> Obtain n
            readFile = public_file.readline()
            n_C = readFile.removeprefix(readFile[:11])
            n_C = n_C.removesuffix(n_C[-1:])
            n_C = int(n_C)            
            
            # Creating the Public Keys
            public_B = Key(e_B, n_B)
            public_C = Key(e_C, n_C)
            
            # User inputs message
            message = input("\nEnter message: ")
            
            # Asks user for recipient
            print("\nUser B (1)")
            print("User C (2)")
            choice = int(input("Who to send to? "))
            
            # Continuous loop until user chooses valid recipient
            ciphertext = ""
            while (True):
                # recipient -> User B
                if (choice == 1):
                    ciphertext = encrypt(message, public_B)
                    break
                    
                # recipient -> User C
                elif (choice == 2):
                    ciphertext = encrypt(message, public_C)
                    break
                    
                # invalid recipient
                else:
                    print("Invalid recipient. Please try again.\n")
                    print("User B (1)")
                    print("User C (2)")
                    choice = int(input("Who to send to? "))
                    
            # Write message to the Public Channel
            public_channel.write(ciphertext)
            
            # Close files and prompt to continue
            public_channel.close()
            public_file.close()
            if (choice == 1):
                print("\nMessage sent to User B.")
            elif (choice == 2):
                print("\nMessage sent to User C.")
            input("(Enter to continue)")        
            
        # User quits
        elif (choice == 3):
            print("\nExiting Terminal A\n")
            break
        
        # Invalid user input
        else:
            print("\nInvalid option.")
            input("(Enter to continue)")
            
    return 0

main()