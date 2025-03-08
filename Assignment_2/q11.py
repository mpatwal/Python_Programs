def caesar_cipher_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  
            shift = key % 26  
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char  
    return encrypted_message

message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (shift value): "))
encrypted_message = caesar_cipher_encrypt(message, key)
print("Encrypted Message:", encrypted_message)
