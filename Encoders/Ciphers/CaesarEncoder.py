from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class CaesarEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 1
        self.paragraphLength = length
        self.name = "Caesar Cipher"

    def ConvertKey(self, key):
        return ord(key.lower()[0]) - 97

    def ParseKey(self, string):
        stripped = str(string).replace(" ", "")
        x = stripped[0]
        if x.isnumeric():
            x = int(x)
        else:
            x = ord(x.lower()) - ord("a")
        return x

    def Encode(self, plaintext, key):
        return ShiftLetters(plaintext, key), key
