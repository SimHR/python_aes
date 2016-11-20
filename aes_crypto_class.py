from Crypto.Cipher import AES
import base64
import os


class Mycrpto:
    def __init__(self, key='ruiY1byeJux5zcCDrV9I/Q=='):
        # type: () -> object
        self.BLOCK_SIZE = 16
        self.PADDING = '0'
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

        self.EncodeAES = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
        self.DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.PADDING)

        self.key = key
        self.secret = base64.b64decode(self.key)

    def enc(self, pure_data):
        cipher = AES.new(self.secret)
        encryp_data = self.EncodeAES(cipher, pure_data)

        return encryp_data

    def dec(self, encryp_data):
        cipher = AES.new(self.secret)

        decryp_data = self.DecodeAES(cipher, encryp_data)
        return decryp_data


data = raw_input("Please input any text: ")

# encrypt with default secret key
crypto = Mycrpto()

enc_data = crypto.enc(data)
print "Encrypted data:", enc_data

dec_data = crypto.dec(enc_data)
print "Decrypted data:", dec_data


# encrypt with custom secret key
secret_key = 'this is the key!'
base64_encoded_key = base64.b64encode(secret_key)
crypto2 = Mycrpto(base64_encoded_key)

enc_data = crypto2.enc(data)
print "Encrypted data:", enc_data

dec_data = crypto2.dec(enc_data)
print "Decrypted data:", dec_data
