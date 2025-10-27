
from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *


class CadenusEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 3
        self.paragraphLength = length
        self.name = "Cadenus Cipher"

    def ConvertKey(self, key):
        return self.ParseKey(key)

    def ParseKey(self, string):
        space_split = string.lower().split(" ")

        if space_split[0].isnumeric():
            numbers = [int(x) for x in space_split]
        elif len(space_split) > 1:
            numbers = [Index(x) for x in space_split]
        else:
            numbers = [Index(x) for x in list(string)]

        return RemoveDuplicates(numbers)
    
    def Encode(self, plaintext, key):
        print(key)
        key_length = len(key)
        length_multiple_requirement = 25 * key_length

        truncated_length = (len(plaintext) // length_multiple_requirement) * length_multiple_requirement
        plaintext = plaintext[:truncated_length]
        
        blocks = MakeBlocks(plaintext, length_multiple_requirement)
        
        ciphertext = ""
        
        for block in blocks:
            cosets = MakeCosets(block, key_length)
            for i, key_char in enumerate(key):
                cosets[i] = RotateList(cosets[i], 25 - key_char)
            
            reduced_keyword = ReducePermutationKeyword(key)
            print(reduced_keyword)

            permuted_cosets = [x for _, x in sorted(zip(key, cosets))]

            ciphertext += Interleave(permuted_cosets)
        
        return plaintext, ciphertext, key
                
        