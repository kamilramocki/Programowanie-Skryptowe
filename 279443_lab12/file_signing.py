from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def save_keys(private_key, public_key):
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("private_key.pem", "wb") as private_file:
        private_file.write(pem_private_key)

    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public_key.pem", "wb") as public_file:
        public_file.write(pem_public_key)


def sign_file(private_key, file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()

    signature = private_key.sign(
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(file_name + ".sig", "wb") as signature_file:
        signature_file.write(signature)


def verify_signature(public_key, file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()

    with open(file_name + ".sig", "rb") as signature_file:
        signature = signature_file.read()

    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature is valid.")
    except:
        print("Signature is invalid.")


private_key, public_key = generate_keys()

save_keys(private_key, public_key)

sign_file(private_key, 'example.txt')

verify_signature(public_key, 'example.txt')
