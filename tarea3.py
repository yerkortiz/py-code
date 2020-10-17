from gost import *
from functools import partial
from pygost.utils import hexdec
from pygost.utils import strxor
from pygost.utils import xrange
from pygost.utils import hexenc
#pt multiplo de 8
pt = hexdec("cacaaaaacacaaaaa".encode("utf-8").hex())
key = hexdec("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode("utf-8").hex())
ct = ecb_encrypt(key, pt)
#dt = ecb_encrypt(key, ct)
print(hexenc(pt))
print(hexenc(ct))
#print(hexenc(dt))
html ="""
<p>Mensaje secreto</p>
<div class='kuznyechik' id='"""+hexenc(ct)+"""'></div>
"""
file = open("index.html","w")
file.write(html)
file.close()