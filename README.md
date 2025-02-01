# 🔐 Text Encryption and Decryption

## 🚀 Overview
This Python program provides encryption and decryption functionalities using two different ciphers:
1. **🔢 Caesar Cipher** - Shifts characters forward or backward by a specified numeric key.
2. **🔀 Substitution Cipher** - Uses a custom key to replace each character uniquely.

Additionally, the program includes a feature to generate a random key for substitution cipher encryption.

## ✨ Features
- ✅ Supports encryption and decryption.
- 🔠 Works with uppercase and lowercase letters, numbers, and special characters.
- 🔑 Allows users to generate a random substitution key.
- 💻 Simple command-line interface for user input.

## 📥 Installation
Ensure you have Python 3 installed on your system. No external dependencies are required.

## 🛠 Usage
1. Run the program:
   ```sh
   python text_encryption.py
   ```
2. Choose an encryption method:
   - Enter `1` for 🔢 Caesar Cipher
   - Enter `2` for 🔀 Substitution Cipher
   - Enter `3` to 🎲 generate a random substitution key
3. Provide the required input:
   - ✍️ Enter the text to encrypt/decrypt.
   - 🔄 Select `e` for encryption or `d` for decryption.
   - 🔢 If using the Caesar Cipher, input a numeric key.
   - 🔑 If using the Substitution Cipher, provide a 26-character key.

## 📌 Example
**🔢 Caesar Cipher Encryption:**
```sh
Enter choice (1, 2, or 3): 1
Enter text: Hello, World!
Encrypt or Decrypt? (e/d): e
Enter numeric key: 3
Result: Khoor, Zruog!
```

**🔀 Substitution Cipher Encryption:**
```sh
Enter choice (1, 2, or 3): 2
Enter text: Hello, World!
Encrypt or Decrypt? (e/d): e
Enter a substitution key: qwertyuiopasdfghjklzxcvbnm
Result: Itssg, Vgksr!
```

## ⚠️ Notes
- 🛑 The Substitution Cipher key must be a valid permutation of characters.
- ⚠️ Ensure to remember the key used for decryption.

## 📜 License
This project is open-source and free to use.

## 👨‍💻 Author
Developed by Naavya. 🚀

