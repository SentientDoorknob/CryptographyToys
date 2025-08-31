from Utility import EncoderEnum
import Interface.DisplayProblem

global_result = None


def Generate(loop=None, gen_new=False):
    global global_result

    if global_result is None or gen_new:
        encoder = EncoderEnum.GetRandom()
        result = encoder.GetPracticeProblem()
        global_result = result

    Interface.CiphertextDisplay.OpenResult(global_result, loop)


if __name__ == "__main__":
    Generate()

