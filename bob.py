import socket
import sqlite3
import base64
import pickle
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import \
        Ed25519PublicKey, Ed25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        #claves privadas y publicas de bob
        SPKb = X25519PrivateKey.generate()
        IKb = X25519PrivateKey.generate()
        OPKb = X25519PrivateKey.generate()

        pem = SPKb.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        data_string_spkb = pickle.dumps(pem)
        
        pem = IKb.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        data_string_ikb = pickle.dumps(pem)
        pem = OPKb.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        data_string_opkb = pickle.dumps(pem)
        #recibir clave de alice
        IKa = b""
        while True:
            packet = connection.recv(4096)
            if not packet: break
            IKa += (packet)
        if IKa:
            IKa = pickle.loads(IKa)
            IKa = IKa.decode('utf-8', 'ignore')
            #dh1 = SPKb.exchange(IKa.public_key()) #primer intercambio
            print(IKa)
            #sock.sendall((data_string))
            break
        else:
            print('no request from', client_address)

    finally:
        connection.close()