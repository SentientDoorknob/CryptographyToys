import math

from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class ColumnarEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 3
        self.paragraphLength = length
        self.name = "Columnar Cipher"

    def ConvertKey(self, key):
        numbers = [ord(i) for i in key]
        keyword = ReducePermutationKeyword(numbers)
        return keyword

    def ParseKey(self, string):
        space_split = string.split(" ")
        numbers = []

        if space_split[0].isnumeric():
            numbers = [int(x) for x in space_split]
        elif len(space_split) > 1:
            numbers = [ord(x) for x in space_split]
        else:
            numbers = [ord(x) for x in list(string)]

        return ReducePermutationKeyword(numbers)

    def Encode(self, plaintext, key):
        keyword_length = len(key)

        truncated_length = (len(plaintext) // keyword_length) * keyword_length
        plaintext = plaintext[:truncated_length]
        
        cosets = MakeCosets(plaintext, keyword_length)

        permutedCosets = []
        for i in range(keyword_length):
            permutedCosets.append(cosets[key[i]])
            
        text = "".join(permutedCosets)
        
        return plaintext, text, key

