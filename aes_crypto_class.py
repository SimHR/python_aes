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

        self.key = "ruiY1byeJux5zcCDrV9I/Q=="
        self.secret = base64.b64decode(self.key)

    def enc(self, pure_data):
        cipher = AES.new(self.secret)
        encryp_data = self.EncodeAES(cipher, pure_data)

        return encryp_data

    def dec(self, encryp_data):
        cipher = AES.new(self.secret)

        decryp_data = self.DecodeAES(cipher, encryp_data)
        return decryp_data


crypto = Mycrpto()

data = raw_input("Please input any text:")
enc_data = crypto.enc(data)
print "Encrypted data:", enc_data

dec_data = crypto.dec(enc_data)
print "Decrypted data:", dec_data
