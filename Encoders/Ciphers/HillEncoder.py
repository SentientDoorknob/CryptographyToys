import random

from Encoders.CipherEncoder import CipherEncoder
from Utility.LinearAlgebra import *


class HillEncoder(CipherEncoder):
    def __init__(self, length):
        self.minKeywordLength = 4
        self.paragraphLength = length
        self.name = "Hill Cipher"

    def ConvertKey(self, key):
        return [ord(x) - 97 for x in key[:4]]

    def ParseKey(self, string):
        stripped = str(string).strip()
        stripped = stripped.replace("[", "").replace("]", "").replace(",", "")

        spaced = stripped.split(" ")

        numbers = []

        if spaced[0].isnumeric():
            numbers = [int(x) for x in spaced]
        elif len(spaced) > 1:
            numbers = [ord(x) - 97 for x in spaced]
        else:
            numbers = [ord(x) - 97 for x in list(stripped)]

        return numbers[:4]

    def Encode(self, plaintext, key):
        keyMatrix = [[key[0], key[1]], [key[2], key[3]]]
        output = ""

        determinant = LinearAlgebra._2x2Det(keyMatrix) % 26

        while math.gcd(determinant, 26) != 1:
            x, y = (random.randint(0, 1), random.randint(0, 1))
            keyMatrix[x][y] += 1
            keyMatrix[x][y] %= 26
            determinant = LinearAlgebra._2x2Det(keyMatrix) % 26

        if math.gcd(LinearAlgebra._2x2Det(keyMatrix) % 26, 26) != 1:
            raise ValueError("Key matrix is not invertible — logic failed")

        vectors = []
        for i in range(0, len(plaintext) - 1, 2):
            vectors.append([[ord(plaintext[i]) - 97], [ord(plaintext[i + 1]) - 97]])

        for vector in vectors:
            returnVector = LinearAlgebra.MxMod(keyMatrix, vector, 26)
            output += chr(returnVector[0][0] + 97)
            output += chr(returnVector[1][0] + 97)

        return output, keyMatrix

