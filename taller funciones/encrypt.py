from procesos.procesos_encrypt import *
while True:
    option = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if option == 'e':
        message = input("Enter the message to encrypt: ").upper()
        key = int(input("Enter the encryption key: "))
        encrypted_message = encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif option == 'd':
        encrypted_message = input("Enter the message to decrypt: ").upper()
        key = int(input("Enter the decryption key: "))
        decrypted_message = decrypt(encrypted_message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")
        
    continue_option = input("Do you want to continue? (y/n): ").lower()
    if continue_option != 'y':
        break

