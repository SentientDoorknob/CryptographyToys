import time
import sys

import Interface.InputCipher
import Interface.DisplayEncoding
from Encoders.Ciphers.CaesarEncoder import *
from Encoders.Ciphers.VignereEncoder import *
from Encoders.Ciphers.AffineEncoder import *
from Encoders.Ciphers.SubstitutionEncoder import *
from Encoders.Ciphers.PermutationEncoder import *
from Encoders.Ciphers.NihilistEncoder import *
from Encoders.Ciphers.HillEncoder import *
from Utility.Tools import *

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
    Interface.EncoderResultDisplay.OpenResult(result, loop)


def OpenCipherInput(loop=None, gen_new=False):
    global global_result

    if global_result is None or gen_new:
        Interface.CipherInput.OpenInput(sys.modules[__name__], loop)
        return

    Interface.EncoderResultDisplay.OpenResult(global_result, loop)


if __name__ == "__main__":
    OpenCipherInput()
