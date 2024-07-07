def caesar_encrypt(plain_text, key):
    encrypted_text = ""
    for letter in plain_text:
        if 'a' <= letter <= 'z':
            cipher = (ord(letter) + key - 97) % 26 + 97
            encrypted_text += chr(cipher)
        elif 'A' <= letter <= 'Z':
            cipher = (ord(letter) + key - 65) % 26 + 65
            encrypted_text += chr(cipher)
        else:
            encrypted_text += letter
    return encrypted_text

def caesar_decrypt(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        if 'a' <= letter <= 'z':
            plain = (ord(letter) - key - 97) % 26 + 97
            decrypted_text += chr(plain)
        elif 'A' <= letter <= 'Z':
            plain = (ord(letter) - key - 65) % 26 + 65
            decrypted_text += chr(plain)
        else:
            decrypted_text += letter
    return decrypted_text

# Ask user for the operation
operation = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()

if operation == 'E':
    # User input for encryption
    plain_text = input('Enter text to encrypt: ')
    key = int(input('Enter encryption key(integer): '))
    encrypted_text = caesar_encrypt(plain_text, key)
    print(f'Encrypted text: {encrypted_text}')
elif operation == 'D':
    # User input for decryption
    cipher_text = input('Enter text to decrypt: ')
    key = int(input('Enter decryption key(integer): '))
    decrypted_text = caesar_decrypt(cipher_text, key)
    print(f'Decrypted text: {decrypted_text}')
else:
    print("Invalid option. Please enter 'E' for encryption or 'D' for decryption.")