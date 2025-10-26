import Text.TextGrabber as text
from Encoders.CipherResult import CipherResult
from Utility.Tools import *


class CipherEncoder:
    minKeywordLength = 1
    paragraphLength = 20
    name = "abstract"

    def GetPracticeProblem(self, plaintext=None, keyword=None):
        if not plaintext:
            plaintext = text.GetParagraph(self.paragraphLength)

        formatted = StringFormat(plaintext)
        plaintext = plaintext.replace("\n", "")

        if (not keyword) | (keyword == ""):
            keyword = self.ConvertKey(self.GetRandomKeyString())
        else:
            keyword = self.ParseKey(keyword.lower())

        plaintext, ciphertext, keyword = self.Encode(formatted, keyword)
        if ciphertext == "":
            ciphertext = "welp someone messed up"

        return CipherResult(plaintext, ciphertext, keyword, self.__str__())

    def Encode(self, plaintext, key):
        return ""

    def ConvertKey(self, key):
        return ""

    def ParseKey(self, string):
        return ""

    def GetRandomKeyString(self):
        key = ""
        while len(key) < self.minKeywordLength:
            key += StringFormat(text.GetWord())
        return key

    def __str__(self):
        return self.name
