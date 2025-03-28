from cryptography.fernet import Fernet

class EncryptDataCore:
    def __init__(self, key: str = "q9kpYwajN4RKCsKFAlzFMfFZd3IUJzIiu2yIcqmGHmM="):
        self._key = key.encode('utf-8')
        self._cipher_suite = Fernet(self._key)

    # descodificar
    def get_decode(self, string: str) -> str:
        data = self._cipher_suite.decrypt(string.strip().encode('utf-8'))
        return data.decode("utf-8")
    
    # codificar
    def get_encode(self, string: str) -> str:
        data = self._cipher_suite.encrypt(string.strip().encode('utf-8'))
        return data.decode("utf-8")