from Crypto.Cipher import AES
import base64
import os


class Mycrpto:
    def __init__(self):
        # type: () -> object
        self.BLOCK_SIZE = 16
        self.PADDING = '0'
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

        self.EncodeAES = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
        self.DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.PADDING)

    def enc(self, pure_data):
        secret = os.urandom(self.BLOCK_SIZE)
        cipher = AES.new(secret)

        encryp_data = self.EncodeAES(cipher, pure_data)

        f = open("key.txt", 'w')
        f.write(secret)
        f.close()

        return encryp_data

    def dec(self, encryp_data):
        f = open("key.txt", "r")
        key = f.read()
        f.close()

        cipher = AES.new(key)

        decryp_data = self.DecodeAES(cipher, encryp_data)
        return decryp_data


crypto = Mycrpto()

data = raw_input("Please input any text:")
enc_data = crypto.enc(data)
print "Encrypted data:", enc_data

dec_data = crypto.dec(enc_data)
print "Decrypted data:", dec_data
