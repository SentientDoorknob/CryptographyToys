from Encoders.CipherEncoder import CipherEncoder
from Utility.Tools import *

class PlayfairEncoder(CipherEncoder):
    
    def ConvertKey(self, key):
        alphabet = [chr(97 + x) for x in range(26)]
        random.shuffle(alphabet)
        return "".join(alphabet)

    def ParseKey(self, string):
        if IsValidKey(StringFormat(string), length=25):
            return StringFormat(string)
        else:
            return self.ConvertKey(None)
        
    def Encode(self, plaintext, key):
        plaintext = StringFormat(plaintext)
        plaintext.replace("j", "i")
        
        