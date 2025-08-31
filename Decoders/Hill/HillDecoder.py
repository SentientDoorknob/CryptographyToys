from Utility.Tools import *
from Decoders.Hill.HillResult import *
from Utility.LinearAlgebra import *


class HillDecoder:
    """

        Note to self: this website is soooo good
        Method Source: https://sites.wcsu.edu/mbxml/html/hill_decrypt_section.html#hill_ciphertext_only

        All matrices are double[][] - see LinearAlgebra.java

        ENCM -> Encryption Matrix.
        DCRM -> Decryption Matrix.
        THHE -> double{{T, H}, {H, E}}

    """

    # CIPHERTEXT -> THHE -> DCRM -> PLAINTEXT
    #                    -> ENCM

    # Returns THHE. Assumes TH is the most common digraph, and HE the second.
    def GetThheMatrix(self, ciphertext):
        digraphs = SplitDigraphs(ciphertext)
        digraph_freq = {}

        uniques = list(set(digraphs))
        for un in uniques: digraph_freq[un] = 0
        print(digraph_freq)
        for graph in digraphs:
            digraph_freq[graph] += 1
        print(digraph_freq)

        digraph_tuples = digraph_freq.items()
        digraph_tuples = sorted(digraph_tuples, key=lambda x: x[1], reverse=True)

        th = digraph_tuples[0][0]
        he = digraph_tuples[1][0]

        return [[Index(th[0]), Index(he[0])], [Index(th[1]), Index(he[1])]]

    # Returns ENCM. Solves for ENCM by subtracting equations. See method.
    def GetEncryptionMatrix(self, thhe):
        con = [[19, 7], [7, 4]]
        return LinearAlgebra.MxMod(thhe, LinearAlgebra._2x2InverseMod(con, 26), 26)

    # Returns DCRM. Solves for DCRM (inverse of ENCM). See method.
    def GetDecryptionMatrix(self, thhe):
        con = [[19, 7], [7, 4]]
        return LinearAlgebra.MxMod(con, LinearAlgebra._2x2InverseMod(thhe, 26), 26)

    # Returns PLAINTEXT. Multiplies digraphs by DCRM. See method.
    def DecryptWithKeyMatrix(self, ciphertext, key):
        digraphs = SplitDigraphs(ciphertext)
        plaintext = ""

        for d in digraphs:
            decrypted = LinearAlgebra.MxMod(key, [[Index(d[0])], [Index(d[1])]], 26)
            plaintext += chr(decrypted[0][0] + 97)
            plaintext += chr(decrypted[1][0] + 97)

        return plaintext

    def Decode(self, ciphertext):
        ciphertext = StringFormat(ciphertext)
        thhe = self.GetThheMatrix(ciphertext)
        dcrm = self.GetDecryptionMatrix(thhe)
        plaintext = self.DecryptWithKeyMatrix(ciphertext, dcrm)

        return HillResult(dcrm, plaintext, ciphertext, thhe)

    def ReEvaluate(self, result, loop):
        result.keyword = self.GetDecryptionMatrix(result.thhe)
        result.plaintext = self.DecryptWithKeyMatrix(result.ciphertext, result.keyword)
        result.Display(loop)

