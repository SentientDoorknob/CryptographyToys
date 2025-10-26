import tkinter as tk

from Utility.Tools import *


class ColumnarResult:
    keyword = ""
    predicted_keyword = ""
    ciphertext = ""
    plaintext = ""
    keyword_len = 0

    is_exiting = False

    def __str__(self):
        return "Columnar Cipher"

    def __init__(self, keyword, plaintext, ciphertext):
        self.keyword = keyword
        self.predicted_keyword = keyword
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.keyword_len = len(keyword)