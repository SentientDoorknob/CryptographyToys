from Decoders.Affine.AffineResult import *


# noinspection PyMethodMayBeStatic
class AffineDecoder:

    """

        Method Source: https://math.asu.edu/sites/default/files/affine.pdf
        ET  -> int[] (index of e, index of t)
        KEY -> int[] (m, b)

    """

    # CIPHERTEXT -> ET -> KEY -> PLAINTEXT -> RESULT

    # Returns ET. Uses 2 highest frequency letters for E and T respectively.
    def GetET(self, ciphertext):
        absoluteFrequency = AbsoluteFrequency(ciphertext)

        sortedFrequency = absoluteFrequency.copy()
        sortedFrequency.sort()

        e = absoluteFrequency.index(sortedFrequency[25])
        t = absoluteFrequency.index(sortedFrequency[24])

        return [e, t]

    # Returns KEY. Given ET and follows method source.
    def GetKeyWithET(self, et):
        e = et[0]
        t = et[1]

        m = ((t - e) * 7) % 26
        c = (e - 4 * m) % 26

        return [m, c]

    # Returns PLAINTEXT. Applies x = (y - b) / m to all ciphertext.
    def DecryptWithKey(self, ciphertext, key):
        m, c = (key[0], key[1])
        output = ""

        for character in ciphertext:
            x = Index(character)
            inverse = ModularInverse(m, 26)
            char = (inverse * (x - c)) % 26
            output += chr(char + 97)

        return output
            

    def Decode(self, ciphertext):
        ciphertext = StringFormat(ciphertext)
        et = self.GetET(ciphertext)
        key = self.GetKeyWithET(et)
        plaintext = self.DecryptWithKey(ciphertext, key)

        return AffineResult(key, plaintext, ciphertext, et)

    def ReEvaluate(self, result, loop):
        result.et = [int(x) for x in result.et]
        result.keyword = self.GetKeyWithET(result.et)
        result.plaintext = self.DecryptWithKey(result.ciphertext, result.keyword)
        result.Display(loop)