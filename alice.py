import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import \
        Ed25519PublicKey, Ed25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
import socket
import pickle
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
connection.connect(server_address)
try:
    IKa = X25519PrivateKey.generate()
    EKa = X25519PrivateKey.generate()
    pem = IKa.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    data_string_ika = pickle.dumps(pem)
    pem = EKa.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    data_string_eka = pickle.dumps(pem)
    #connection.sendall((data_string_ika))
    #connection.sendall((data_string_eka))


finally:
    print('closing encypter socket')
    connection.close()