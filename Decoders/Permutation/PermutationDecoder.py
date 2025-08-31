from Decoders.Permutation.PermutationResult import PermutationResult
from Utility.Tools import *
from Utility.Digram import DigramScores
from Decoders.Permutation.PermutationResult import *


class PermutationDecoder:
    """

        Method Source: https://homepages.math.uic.edu/~leon/mcs425-s08/handouts/breaking_tranposition_cipher.pdf

        PAIRS -> How likely 2 Columns are to be next to each other.
        KEY -> Array of integers, ascending order.

    """

    MAX_KEYWORD_LENGTH = 30

    # CIPHERTEXT -> PAIRS -> KEY -> PLAINTEXT

    # UTIL -> EvaluateCiphertext
    def EvaluateColumnPair(self, c1, c2):
        if c1 == c2:
            return -10

        column_size = min(len(c1), len(c2))

        total = 0
        for i in range(column_size):
            l, m = Index(c1[i]), Index(c2[i])
            total += DigramScores[l][m]

        return total / column_size

    # Returns PAIRS. Recursively follows method with incrementing keyword lengths.
    def EvaluateCiphertext(self, ciphertext, length):
        if length >= self.MAX_KEYWORD_LENGTH:
            return None

        cosets = MakeCosets(ciphertext, length)
        results = []

        for _ in range(length):
            results.append([0 for i in range(length)])

        num_positives = 0

        for i in range(length):
            c1 = cosets[i]
            for j in range(length):
                c2 = cosets[j]

                score = self.EvaluateColumnPair(c1, c2)
                results[i][j] = score

                if score > 0:
                    num_positives += 1
        
        print(f"Keyword Length: {length}, Positives: {num_positives}")
        if num_positives >= (length - 2):
            return results

        return self.EvaluateCiphertext(ciphertext, length + 1)

    # Returns KEY. See method - follows path of adjacent columns.
    def GetKeyword(self, pairs):
        active_column = 1
        length = len(pairs)

        for i in range(length):
            is_negative = all(x < 0 for x in GetColumn(pairs, i))
            if is_negative:
                active_column = i

        keyword = [0 for _ in range(length)]

        for i in range(length):
            keyword[i] = active_column

            max_in_column = max(pairs[active_column])
            active_column = (pairs[active_column]).index(max_in_column)

        return ReducePermutationKeyword(keyword)

    # Returns PLAINTEXT. Rearranges columns.
    def DecryptWithKeyword(self, ciphertext, keyword):
        length = len(keyword)
        cosets = MakeCosets(ciphertext, length)

        permuted_cosets = ["" for _ in range(length)]

        for i in range(length):
            permuted_cosets[i] = cosets[keyword[i]]

        return Interleave(permuted_cosets)

    def Decode(self, ciphertext):
        print("DECODING")
        text = StringFormat(ciphertext)
        print(text)
        pairs = self.EvaluateCiphertext(text, 3)
        print(pairs)
        
        if pairs is None:
            return PermutationResult([1, 2, 3, 4], f"nosolutionfoundifidontputthisinitcrashessoherewearehowisyourdaygoing", ciphertext)
        
        keyword = self.GetKeyword(pairs)
        print(keyword)
        plaintext = self.DecryptWithKeyword(text, keyword)
        print(plaintext)

        return PermutationResult(keyword, plaintext, text)

    def ReEvaluate(self, result, loop):
        result.keyword_len = len(result.keyword)
        result.plaintext = StringFormat(self.DecryptWithKeyword(result.ciphertext, result.keyword))
        result.Display(loop)



