from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os


def pad(data):
    length = 16 - (len(data) % 16)
    return data + bytes([length]) * length


def unpad(data):
    length = data[-1]
    return data[:-length]


def encrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext))

    with open(file_name + '.enc', 'wb') as file:
        file.write(cipher.iv)
        file.write(ciphertext)


def decrypt_file(file_name, key):
    with open(file_name, 'rb') as file:
        iv = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext))

    with open(file_name[:-4], 'wb') as file:
        file.write(plaintext)


key = get_random_bytes(16)

encrypt_file('example.txt', key)

decrypt_file('example.txt.enc', key)
