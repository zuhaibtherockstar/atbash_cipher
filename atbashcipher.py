# atbash_cipher.py
# Author: Zuhaib
# Description: A simple implementation of the classical Atbash Cipher in Python.

def atbash_cipher(text):
    """Encrypts or decrypts text using the Atbash Cipher."""
    result = ""

    for char in text:
        # Handle uppercase letters
        if char.isupper():
            # 'A' ↔ 'Z' → formula: new_char = 'Z' - (char - 'A')
            result += chr(90 - (ord(char) - 65))
        # Handle lowercase letters
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        # Preserve non-alphabetic characters
        else:
            result += char

    return result


# --- Main Program ---
if __name__ == "__main__":
    print("🔐 Welcome to the Atbash Cipher Program 🔐")
    plaintext = input("Enter your text: ")

    # Encrypt the input
    encrypted = atbash_cipher(plaintext)
    print(f"\nEncrypted Text: {encrypted}")

    # Decrypt to verify (Atbash is symmetric)
    decrypted = atbash_cipher(encrypted)
    print(f"Decrypted Text: {decrypted}")
