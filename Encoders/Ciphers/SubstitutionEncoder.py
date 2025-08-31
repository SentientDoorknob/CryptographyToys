import random
from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *

class SubstitutionEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 1
        self.paragraphLength = length
        self.name = "Substitution Cipher"

    def Encode(self, plaintext, key):
        plaintext = plaintext.upper()
        key = key.lower()
        
        if len(key) < 26:
            raise KeyError(f"Invalid Substitution Key: {key}")
        
        for i in range(26):
            plaintext = plaintext.replace(chr(65 + i), key[i])
            
        return plaintext.lower(), key

    def ConvertKey(self, key):
        alphabet = [chr(97 + x) for x in range(26)]
        random.shuffle(alphabet)
        return "".join(alphabet)

    def ParseKey(self, string):
        if IsValidKey(StringFormat(string)):
            return StringFormat(string)
        else:
            return self.ConvertKey(None)