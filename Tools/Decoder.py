import Interface.InputCipher
from Decoders.Affine.AffineDecoder import *
from Decoders.Hill.HillDecoder import *
from Decoders.Nihilst.NihilstDecoder import *
from Decoders.Permutation.PermutationDecoder import *
from Decoders.Vignere.VignereDecoder import *
from Decoders.Columnar.ColumnarDecoder import *

ciphers = {"Vignere Cipher": VignereDecoder(),
           "Affine Cipher": AffineDecoder(),
           "Permutation Cipher": PermutationDecoder(),
           "Hill Cipher": HillDecoder(),
           "Nihilist Cipher": NihilistDecoder(),
           "Columnar Cipher": ColumnarDecoder()}


global_result = None


def AfterCipherInput(text, cipher_index, textbox, use_keyword, success, loop):
    global global_result
    #print(f"returned to decoder main, {textbox} {use_keyword}")
    if not success: import MainFile; MainFile.OpenInput(loop); return

    decoder = ciphers[cipher_index]
    result = decoder.Decode(text)
    global_result = result
    result.Display(loop)


def OpenCipherInput(module_name, loop=None, gen_new=False):
    global global_result

    if global_result is None or gen_new:
        Interface.InputCipher.OpenInput(module_name, loop)
        return

    global_result.Display(loop)
