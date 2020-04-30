from eth_keyfile import extract_key_from_keyfile, create_keyfile_json
import getpass
from codecs import encode, decode
from json import dumps


class Authentication:

    @staticmethod
    def get_private_key_from_keyfile_by_explicit_password(file: str, password: str) -> bytes:
        private_key = extract_key_from_keyfile(file, password.encode())
        encoded = encode(private_key, "hex")
        decoded_private_key = encoded.decode()
        return decoded_private_key

    @staticmethod
    def get_private_key_from_keyfile_by_asking_password(file: str) -> bytes:
        password = getpass.getpass("Password: ")
        private_key = extract_key_from_keyfile(file, password.encode())
        encoded = encode(private_key, "hex")
        decoded_private_key = encoded.decode()
        return decoded_private_key

    @staticmethod
    def encrypt_keyfile(file: str, private_key: str, password: str):
        encoded_private_key = decode(private_key.encode(), "hex")
        output_dict = create_keyfile_json(encoded_private_key, password.encode())
        output_str = dumps(output_dict)
        output_double_quoted = output_str.replace("'", '"') # Replace single quote to double quote
        with open(file, "w") as f:
            f.write(output_double_quoted)
        print(f"{file} is created")

    @staticmethod
    def decrypt_keyfile(file: str, password: str):
        private_key = extract_key_from_keyfile(file, password.encode())
        encoded = encode(private_key, "hex")
        decoded_private_key = encoded.decode()
        print(f"{decoded_private_key}")
