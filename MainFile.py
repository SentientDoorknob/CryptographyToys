import Interface.InputCipher
import Interface.SelectTool
from Tools import HillClimber, Generator, Decoder, Encoder, Profiler, Formatter

main_functions = [("Encode", Encoder.OpenCipherInput, "encode.png"),
                  ("Decode", Decoder.OpenCipherInput, "decode.png"),
                  ("Practice Problems", Generator.Generate, "generate.png"),
                  ("Cipher Profiler", Profiler.OpenTextInput, "magnifier.png"),
                  ("Substitution", HillClimber.OpenCipherInput, "swap.png"),
                  ("Formatter", Formatter.OpenTool, "format.png"),]


def OpenInput(loop=None):
    Interface.SelectTool.OpenInput(loop)
    
def ClearGlobals():
    print("Clearing globals")
    Encoder.global_result = None
    Decoder.global_result = None
    Generator.global_result = None
    Profiler.global_result = None
    HillClimber.global_result = None
    


if __name__ == "__main__":
    OpenInput()

