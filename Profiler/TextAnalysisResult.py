
x = """
Metrics to Include:

Text
Index of Coincidence
Chi Squared
Frequency Analysis
Common Bigrams
Friedman Test
Entropy
"""


class TextAnalysisResult:
    text = ""
    indexOC = 0
    friedmanTest = 0
    chiSquared = 0
    entropy = 0
    triEntropy = 0
    cosineFitness = 0
    substitutionFitness = 0
    englishFitness = 0
    letterFrequencies = [0 for i in range(26)]
    periodLength = 0
    commonBigrams = []
    commonMonograms = []

    
