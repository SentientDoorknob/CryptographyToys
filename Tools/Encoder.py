import sys

import Interface.DisplayEncoding
import Interface.InputCipher
from Encoders.Ciphers.AffineEncoder import *
from Encoders.Ciphers.CaesarEncoder import *
from Encoders.Ciphers.HillEncoder import *
from Encoders.Ciphers.NihilistEncoder import *
from Encoders.Ciphers.PermutationEncoder import *
from Encoders.Ciphers.SubstitutionEncoder import *
from Encoders.Ciphers.VignereEncoder import *

length = 0

ciphers = {"Caesar Cipher": CaesarEncoder(length),
           "Vignere Cipher": VignereEncoder(length),
           "Affine Cipher": AffineEncoder(length),
           "Substitution Cipher": SubstitutionEncoder(length),
           "Permutation Cipher": PermutationEncoder(length),
           "Hill Cipher": HillEncoder(length),
           "Nihilist Cipher": NihilistEncoder(length)}


global_result = None


def AfterCipherInput(text, cipher_index, keyword, use_keyword, success, loop):
    global global_result
    print(f"returned to encoder main, {keyword} {use_keyword}")
    if not success: import MainFile; MainFile.OpenInput(loop); return
    encoder = ciphers[cipher_index]

    result = encoder.GetPracticeProblem(plaintext=text, keyword=keyword)
    global_result = result
    Interface.DisplayEncoding.OpenResult(result, loop)


def OpenCipherInput(loop=None, gen_new=False):
    global global_result

    if global_result is None or gen_new:
        Interface.InputCipher.OpenInput(sys.modules[__name__], loop)
        return

    Interface.DisplayEncoding.OpenResult(global_result, loop)


if __name__ == "__main__":
    OpenCipherInput()
