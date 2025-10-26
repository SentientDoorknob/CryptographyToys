from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class VignereEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 3
        self.paragraphLength = length
        self.name = "Vignere Cipher"

    def Encode(self, plaintext, key):
        keyword_length = len(key)
        cosets = MakeCosets(plaintext, keyword_length)

        for i in range(keyword_length):
            cosets[i] = ShiftLetters(cosets[i], ord(key[i]) - 97)

        return plaintext, Interleave(cosets), key

    def ConvertKey(self, key):
        return self.ParseKey(key)

    def ParseKey(self, string):
        return StringFormat(string)
