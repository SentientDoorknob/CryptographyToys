from Decoders.PolySubstitution.PolySubstitutionDecoder import PolySubstitutionDecoder
import Interface.InputHillclimber

global_result=None
decoder = PolySubstitutionDecoder()

def AfterCipherInput(text, max_iterations, threshold, success, loop):
    global global_result
    if not success: import MainFile; MainFile.OpenInput(loop); return

    result = decoder.Decode(text, max_iterations, threshold)
    if result is None:
        return
    global_result = result
    global_result.Display(loop)


def OpenCipherInput(module, loop=None, gen_new=True):
    global global_result

    if global_result is None or gen_new:
        Interface.InputSubstitution.OpenInput(module, loop)
        return

    global_result.Display(loop)