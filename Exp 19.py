from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt(plaintext, key, iv):
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()

    padded_plaintext = padder.update(plaintext) + padder.finalize()


    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    
    return ciphertext


def decrypt(ciphertext, key, iv):

    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()

    return plaintext


key = os.urandom(24)  
iv = os.urandom(algorithms.TripleDES.block_size // 8)
plaintext = b'This is a test message'

# Encryption
ciphertext = encrypt(plaintext, key, iv)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext, key, iv)
print("Decrypted Text:", decrypted_text.decode())
