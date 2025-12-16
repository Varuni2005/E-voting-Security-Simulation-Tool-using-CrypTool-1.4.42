from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class AESModule:
    def __init__(self):
        self.key = AESGCM.generate_key(bit_length=256)

    def encrypt(self, text):
        aes = AESGCM(self.key)
        nonce = os.urandom(12)
        encrypted = aes.encrypt(nonce, text.encode(), None)
        return nonce.hex() + ":" + encrypted.hex()

    def decrypt(self, text):
        nonce_hex, data_hex = text.split(":")
        nonce = bytes.fromhex(nonce_hex)
        data = bytes.fromhex(data_hex)
        aes = AESGCM(self.key)
        return aes.decrypt(nonce, data, None).decode()
