import Interface.DisplayProfile
import Interface.InputText
from Profiler.Analyser import *
import sys

global_result = None
no_bigrams = 7

def OnTextInput(success, text, loop):
    if not success: import MainFile; MainFile.OpenInput(loop); return

    global global_result
    global_result = Analyse(text, no_bigrams)
    Interface.AnalysisDisplay.ShowResult(global_result, loop)


def OpenTextInput(loop=None, gen_new=False):
    global global_result

    if not global_result or gen_new:
        Interface.TextInput.OpenInput(sys.modules[__name__], loop)
        return

    Interface.AnalysisDisplay.ShowResult(global_result, loop)
