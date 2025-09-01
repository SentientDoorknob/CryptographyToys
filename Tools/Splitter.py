import Interface.InputText
import Interface.ToolSplitter
from Utility.Tools import *

global_result = None


def OnTextInput(success, text, loop):
    if not success: import MainFile; MainFile.OpenInput(loop); return
    
    global global_result
    
    text = StringFormat(text)
    global_result = text

    Interface.ToolSplitter.OpenSplitter(text, loop)


def OpenCosetInterface(module_name, loop, gen_new=False):
    global global_result
    
    if global_result is None or gen_new:
        Interface.InputText.OpenInput(module_name, loop)
        return
    
    Interface.ToolSplitter.OpenSplitter(global_result, loop)