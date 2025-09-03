import Interface.InputCipher
import Interface.SelectTool
from Tools import HillClimber, Generator, Decoder, Encoder, Profiler, Formatter, Splitter, Merger

main_functions = [("Encode", lambda loop: Encoder.OpenCipherInput(Encoder, loop), "encode.png"),
                  ("Decode", lambda loop: Decoder.OpenCipherInput(Decoder, loop), "decode.png"),
                  ("Practice Problems", Generator.Generate, "generate.png"),
                  ("Cipher Profiler", lambda loop: Profiler.OpenTextInput(Profiler, loop), "magnifier.png"),
                  ("Substitution", lambda loop: HillClimber.OpenCipherInput(HillClimber, loop), "swap.png"),
                  ("Formatter", Formatter.OpenTool, "format.png"),
                  ("Splitter", lambda loop: Splitter.OpenCosetInterface(Splitter, loop), "split.png"),
                  ("Merger", Merger.OpenInterleaver, "merge.png"),]

def OpenInput(loop=None):
    Interface.SelectTool.OpenInput(loop)
    
def ClearGlobals():
    print("Clearing globals")
    Encoder.global_result = None
    Decoder.global_result = None
    Generator.global_result = None
    Profiler.global_result = None
    HillClimber.global_result = None
    Splitter.global_result = None

if __name__ == "__main__":
    OpenInput()

