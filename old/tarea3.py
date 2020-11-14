from gost import *
#gost.py es parte de la libreria, pero solo el archivo.
#como es un standar ruso, gran parte de lo que encontré en internet
#estaba en ese idioma así que el camino más corto fue ver directamente
#la implementación del algoritmo y ver como usarlo
#el resto de funciones de pygost son para codificar y decodificar entre arreglos de bytes y hexadecimal
from functools import partial
from pygost.utils import hexdec
from pygost.utils import strxor
from pygost.utils import xrange
from pygost.utils import hexenc
#pip instal pygost
#ejecutar con python3 tarea3.py

pt = hexdec("holaaaaa".encode("utf-8").hex())
key = hexdec("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".encode("utf-8").hex())
ct = ecb_encrypt(key, pt)
#dt = ecb_encrypt(key, ct)
print('mensaje en texto plano: ' + hexenc(pt))
print('mensaje encriptado: ' + hexenc(ct))
#print(hexenc(dt))
html ="""
<p>Mensaje secreto</p>
<div class='kuznyechik' id='"""+hexenc(ct)+"""'></div>
"""
file = open("index.html","w")
file.write(html)
file.close()