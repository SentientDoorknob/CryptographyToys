from Utility.Tools import *
from Decoders.Permutation.PermutationDecoder import PermutationDecoder
from Utility.Digram import DigramScores
from Decoders.Columnar.ColumnarResult import ColumnarResult


class ColumnarDecoder:
    """
            Transpose into permutation cipher, then solve.
    """
    
    permutationDecoder = PermutationDecoder()
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
    
    
    def GetPairs(self, ciphertext, length):
        if length >= self.MAX_KEYWORD_LENGTH:
            return None, None
        
        inverse_transpose_length = len(ciphertext) // length
        text = Transpose(ciphertext, n=inverse_transpose_length)
        ##print(len(ciphertext), length, len(ciphertext) % length, inverse_transpose_length, text)
        pairs = []
        
        cosets = MakeCosets(text, length)

        for _ in range(length):
            pairs.append([0 for i in range(length)])
            
        positives = 0
        for i in range(length):
            c1 = cosets[i]
            
            for j in range(length):
                c2 = cosets[j]

                score = self.EvaluateColumnPair(c1, c2)
                pairs[i][j] = score

                if score > 0:
                    positives += 1

        if positives >= (length - 1): 
            return pairs, text

        return self.GetPairs(ciphertext, length + 1)

    def Decode(self, ciphertext):
        ciphertext = StringFormat(ciphertext)
        pairs, t_text = self.GetPairs(ciphertext, 3)
        
        if pairs is None:
            return ColumnarResult([1, 2, 3, 4], f"nosolutionfoundifidontputthisinitcrashessoherewearehowisyourdaygoing", ciphertext)
        
        keyword = self.permutationDecoder.GetKeyword(pairs)
        plaintext = self.permutationDecoder.DecryptWithKeyword(t_text, keyword)
        
        return ColumnarResult(keyword, plaintext, ciphertext)