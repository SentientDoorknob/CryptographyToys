from Utility.Tools import *
from Decoders.Vignere.VignereResult import *


class VignereDecoder:
    def __str__(self):
        return "Vignere Cipher"

    """
        Method Source: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html and subsequent articles

        IOC -> Index of Coincidence
        IOCD -> Calculated IoC - English IoC.
        KEYLEN -> Length of keyword.
        KEY -> String of letters, not AIs.
    """

    VIGNERE_THRESHOLD = 0.005
    MAX_KEYWORD_LENGTH = 30

    # CIPHERTEXT -> KEYLEN -> KEY -> PLAINTEXT

    # Returns IOCD. Generates cosets given length and calculates average IoC.
    def TryKeywordLength(self, ciphertext, length):
        cosets = MakeCosets(ciphertext, length)
        total = sum([IndexOfCoincidence(s) for s in cosets])
        average = total / length
        return abs(average - ENGLISH_IOC)

    # Returns KEYLEN. Tries lengths up to max, and gets smallest less than vignere threshold.
    def GetKeywordLength(self, ciphertext):
        results = [self.TryKeywordLength(ciphertext, i) for i in range(1, VignereDecoder.MAX_KEYWORD_LENGTH)]
        #print(results)
        threshold = list(filter(lambda x: x < VignereDecoder.VIGNERE_THRESHOLD, results))
        if len(threshold) == 0: return 1
        return results.index(threshold[0]) + 1

    # Returns KEY. For each coset, runs X2 analysis - see method.
    def GetKeywordWithLength(self, ciphertext, length):
        cosets = MakeCosets(ciphertext, length)
        keyword = ""

        for coset in cosets:
            minX2 = 100
            mindex = 0

            for i in range(26):
                coset = ShiftLetters(coset, -1)
                cosetX2 = XSquared(coset)

                if cosetX2 < minX2:
                    minX2 = cosetX2
                    mindex = i

            index = (mindex + 1) % 26
            keyword += chr(index + 97)

        return keyword

    # Returns PLAINTEXT. Shifts cosets by respective keyword char.
    def DecryptWithKeyword(self, ciphertext, keyword):
        cosets = MakeCosets(ciphertext, len(keyword))

        for i in range(len(keyword)):
            cosets[i] = ShiftLetters(cosets[i], Index(keyword[i]) * -1)

        return Interleave(cosets)

    # Returns RESULT.
    def Decode(self, ciphertext):
        ciphertext = StringFormat(ciphertext)
        length = self.GetKeywordLength(ciphertext)
        keyword = self.GetKeywordWithLength(ciphertext, length)
        plaintext = self.DecryptWithKeyword(ciphertext, keyword)
        return VignereResult(keyword, plaintext, ciphertext)

    def ReEvaluate(self, result, loop):
        result.keyword = StringFormat(result.keyword)
        result.plaintext = self.DecryptWithKeyword(result.ciphertext, result.keyword)
        result.keyword_len = len(result.keyword)
        result.Display(loop)
