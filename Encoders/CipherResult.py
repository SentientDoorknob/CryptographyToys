class CipherResult:
    def __init__(self, plain, cipher, keyword, encoder):
        self.plaintext = plain
        self.ciphertext = cipher
        self.keyword = keyword
        self.encoder = encoder
