from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class NihilistEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 3
        self.paragraphLength = length
        self.name = "Nihilist Cipher"

    def ConvertKey(self, key):
        return self.ParseKey(key)

    def ParseKey(self, string):
        return StringFormat(string)

    def Encode(self, plaintext, key):
        input_ints = []
        for char in plaintext:
            input_ints.append(GetPolybiusCoordinates(char))

        cosets = MakeCosets(input_ints, len(key), False)
        output_cosets = [[] for _ in range(len(key))]

        for i in range(len(key)):
            keychar = GetPolybiusCoordinates(key[i])
            output_cosets[i] = [x + keychar for x in cosets[i]]

        output_ints = InterleaveList(output_cosets)
        return plaintext, " ".join([str(x) for x in output_ints]), key
