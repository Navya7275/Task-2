import string
import random

def caesar_cipher(text, key, decrypt=False):
    """Encrypts or decrypts a text using the Caesar Cipher."""
    if decrypt:
        key = -key
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def generate_random_key():
    """Generates a random 26-letter permutation key for substitution cipher."""
    alphabet = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def substitution_cipher(text, key, decrypt=False):
    """Encrypts or decrypts a text using a simple substitution cipher."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    key = key[:len(alphabet)]
    
    if len(set(key)) != len(alphabet) or any(c not in alphabet for c in key):
        raise ValueError("Key must be a unique permutation of the allowed characters.")
    
    if decrypt:
        table = str.maketrans(key, alphabet)
    else:
        table = str.maketrans(alphabet, key)
    
    return text.translate(table)

def main():
    print("Choose encryption method:")
    print("1. Caesar Cipher")
    print("2. Substitution Cipher")
    print("3. Generate Random Key for Substitution Cipher")
    choice = input("Enter choice (1, 2, or 3): ")
    
    if choice == '3':
        print("Generated Key:", generate_random_key())
        return
    
    text = input("Enter text: ")
    action = input("Encrypt or Decrypt? (e/d): ").lower()
    decrypt = action == 'd'
    
    if choice == '1':
        key = int(input("Enter numeric key: "))
        result = caesar_cipher(text, key, decrypt)
    elif choice == '2':
        key = input("Enter a substitution key of correct length: ")
        result = substitution_cipher(text, key, decrypt)
    else:
        print("Invalid choice.")
        return
    
    print("Result:", result)
    
if __name__ == "__main__":
    main()
