# encryption.py
from cryptography.fernet import Fernet
import os

# Generate and save a key (only once)
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved as secret.key")
    else:
        print("Key already exists.")

# Load key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"{filename} encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted_data = enc_file.read()
    decrypted = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"{filename} decrypted successfully!")