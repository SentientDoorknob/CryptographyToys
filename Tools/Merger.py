import Interface.ToolMerger
from Utility.Tools import *


def AfterTextInput(texts, loop):
    text = Interleave(texts)
    Interface.ToolMerger.OpenTextDisplay(text, loop)

def OpenInterleaver(loop):
    Interface.ToolMerger.OpenMerger(loop)