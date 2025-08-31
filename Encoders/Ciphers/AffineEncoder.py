from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class AffineEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 2
        self.paragraphLength = length
        self.name = "Affine Cipher"

    def ConvertKey(self, key):
        m = ord(key[0]) - 97
        c = ord(key[1]) - 97
        return [m, c]

    def ParseKey(self, string):
        stripped = str(string).strip()
        stripped = stripped.replace("[", "").replace("]", "").replace(",", "")
        return stripped.split(" ")[:2]

    def Encode(self, plaintext, key):
        output = ""

        m, c = int(key[0]), int(key[1])

        while math.gcd(m, 26) != 1:
            m = (m + 1) % 26 

        for char in plaintext:
            x = ord(char) - 97
            y = (m * x + c) % 26
            output += chr(y + 97)

        return output, [m, c]
