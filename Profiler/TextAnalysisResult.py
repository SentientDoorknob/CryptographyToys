
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
    length = 0
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
    digraphicIndexOC = 0
    commonBigrams = []
    commonMonograms = []
    
    def __str__(self):
        return (f"""
IOC:  {self.indexOC}
DIOC: {self.digraphicIndexOC}
FMT:  {self.friedmanTest}
X2:   {self.chiSquared}
E:    {self.entropy}
3E:   {self.triEntropy}
F:    {self.englishFitness}
SF:   {self.substitutionFitness}
        """)
    
    def __iter__(self):
        yield [self.indexOC, self.digraphicIndexOC, self.friedmanTest, self.chiSquared, self.entropy, self.triEntropy, self.englishFitness, self.substitutionFitness]

    
