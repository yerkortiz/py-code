from pygost.gost3413 import cbc_decrypt
from pygost.gost3413 import cbc_encrypt
from pygost.gost3413 import ecb_decrypt
from pygost.gost3413 import ecb_encrypt
from pygost.gost3412 import GOST3412Kuznechik
from pygost.utils import hexdec
from pygost.gost3413 import pad2
from pygost.gost3413 import unpad2
from pygost.utils import hexenc
import binascii
from os import urandom
from random import randint
'''
class GOST3412KuznechikModesTest():
    key = hexdec("8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef")
    ciph = GOST3412Kuznechik(key)
    plaintext = ""
    plaintext += "1122334455667700ffeeddccbbaa9988"
    plaintext += "00112233445566778899aabbcceeff0a"
    plaintext += "112233445566778899aabbcceeff0a00"
    plaintext += "2233445566778899aabbcceeff0a0011"
    iv = hexdec("1234567890abcef0a1b2c3d4e5f0011223344556677889901213141516171819")
    def test_ecb_vectors(self):
        ciphtext = ""
        ciphtext += "7f679d90bebc24305a468d42b9d4edcd"
        ciphtext += "b429912c6e0032f9285452d76718d08b"
        ciphtext += "f0ca33549d247ceef3f5a5313bd4b157"
        ciphtext += "d0b09ccde830b9eb3a02c4c5aa8ada98"
        print(hexenc(ecb_encrypt(self.ciph.encrypt, 16, hexdec(self.plaintext))))
        print(hexenc(ecb_decrypt(self.ciph.decrypt, 16, hexdec(ciphtext))))
    def test_ecb_symmetric(self):
        for _ in range(100):
            pt = pad2(urandom(randint(0, 16 * 2)), 16)
            ciph = GOST3412Kuznechik(urandom(32))
            ct = ecb_encrypt(ciph.encrypt, 16, pt)
            dt = ecb_decrypt(ciph.decrypt, 16, ct)
            print(hexenc(self.key))
            #print(hexenc(dt))
'''
'''
key = ""
key += "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s = key.encode("utf-8").hex()
ciph = GOST3412Kuznechik(hexdec(s))
#print(s)
plaintext = ""
plaintext += "holaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode("utf-8").hex()
texto_enc = hexenc(ecb_encrypt(ciph.encrypt, 16, hexdec(plaintext)))
texto_dec = hexenc(ecb_decrypt(ciph.decrypt, 16, hexdec(texto_enc)))
print(plaintext)
print(texto_enc)
print(texto_dec)
'''

pt = hexdec("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode("utf-8").hex())
ciph = GOST3412Kuznechik(urandom(32))
ct = ecb_encrypt(ciph.encrypt, 16, pt)
dt = ecb_decrypt(ciph.decrypt, 16, ct)
print(hexenc(pt))
print(hexenc(ct))
print(hexenc(dt))