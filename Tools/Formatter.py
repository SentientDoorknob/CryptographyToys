import Interface.ToolFormatter
from Utility.Tools import *

formats = {
    "String Format": StringFormat,
    "Number Format": NumberFormat,
    "Digit Format": DigitFormat,
}

def OpenTool(loop):
    Interface.ToolFormatter.OpenFormatter(loop)