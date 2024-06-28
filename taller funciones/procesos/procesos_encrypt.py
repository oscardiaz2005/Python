def encrypt_character(character, b):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if character in alphabet:
        index = alphabet.index(character)
        new_position = (index + b) % len(alphabet)
        return alphabet[new_position]
    else:
        return character  

def decrypt_character(encrypted_character, b):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if encrypted_character in alphabet:
        index = alphabet.index(encrypted_character)
        new_position = (index - b) % len(alphabet)
        return alphabet[new_position]
    else:
        return encrypted_character 


def encrypt(message, b):
    encrypted_message = ""
    for character in message:
        encrypted_message += encrypt_character(character, b)
    return encrypted_message


def decrypt(encrypted_message, b):
    decrypted_message = ""
    for character in encrypted_message:
        decrypted_message += decrypt_character(character, b)
    return decrypted_message



