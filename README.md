==================================================
               ATBASH CIPHER IN PYTHON
==================================================

Author: Zuhaib
Repository Name: atbash_cipher
Language: Python
Date: October 2025

--------------------------------------------------
OVERVIEW
--------------------------------------------------
The Atbash Cipher is one of the oldest known substitution ciphers.
It works by reversing the alphabet, so:

A ↔ Z
B ↔ Y
C ↔ X
...
Z ↔ A

For example:
HELLO becomes SVOOL

It is a simple yet elegant cipher that demonstrates
the core idea of cryptography — transforming readable
text into a hidden form.

--------------------------------------------------
FEATURES
--------------------------------------------------
- Encrypts and decrypts text symmetrically
- Works with both uppercase and lowercase letters
- Preserves spaces, numbers, punctuation, and emojis
- Written in clean and readable Python code
- Ideal for understanding substitution ciphers

--------------------------------------------------
EXAMPLE RUN
--------------------------------------------------
🔐 Welcome to the Atbash Cipher Program 🔐
Enter your text: Hello, World!

Encrypted Text: Svool, Dliow!
Decrypted Text: Hello, World!

--------------------------------------------------
HOW IT WORKS
--------------------------------------------------
1. Each letter is mirrored across the alphabet.
   Example: A (1st) ↔ Z (26th), B (2nd) ↔ Y (25th)
2. The program checks if each character is:
   - Uppercase: Converts using ASCII range 65–90
   - Lowercase: Converts using ASCII range 97–122
3. Non-alphabetic characters are left unchanged.

--------------------------------------------------
CODE SUMMARY
--------------------------------------------------
Function: atbash_cipher(text)
- Takes a string as input
- Loops through each character
- Replaces alphabetic characters with their reverse
- Returns the encrypted (or decrypted) string

Since Atbash is symmetric, the same function
works for both encryption and decryption.

--------------------------------------------------
USAGE
--------------------------------------------------
1. Clone the repository:
   git clone https://github.com/yourusername/atbash_cipher.git

2. Run the script:
   python atbash_cipher.py

3. Enter your text when prompted.
   The program will display the encrypted
   and decrypted results.

--------------------------------------------------
REAL-WORLD CONNECTION
--------------------------------------------------
Although the Atbash Cipher is not secure by
modern standards, it introduces the basic concept
of substitution used in more advanced ciphers like
Caesar and Vigenère.

It’s a great way to see how ancient logic inspired
modern cryptographic algorithms.

--------------------------------------------------
REFLECTION
--------------------------------------------------
The Atbash Cipher’s simplicity is what makes it
so fascinating. With just a few lines of Python,
we can bring an ancient encryption method to life.

It reminds us that even simple patterns and logic
can lead to deep insights — both in programming
and in understanding human creativity.
--------------------------------------------------
