import tkinter as tk
from Utility.Tools import *


class PolySubstitutionResult:
    keywords = []
    predicted_keywords = []
    ciphertext = ""
    plaintext = ""
    iterations = 0

    def __str__(self):
        return "Poly-Substitution Cipher"

    def __init__(self, keywords, plaintext, ciphertext, iterations):
        self.keyword = keywords
        self.predicted_keywords = keywords
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.iterations = iterations

    def Display(self, loop):
        #print(self.iterations)
        #print(self.keywords)
        #print(self.ciphertext)
        loop.destroy()