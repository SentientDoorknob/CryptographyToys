from Profiler.TextAnalysisResult import *
from Decoders.Vignere.VignereDecoder import VignereDecoder
from Utility.Tools import *

vignere_decoder = VignereDecoder()

def Analyse(text, no_bigrams):
    text = StringFormat(text)
    result = TextAnalysisResult()
    result.text = text
    result.indexOC = round(IndexOfCoincidence(text), 4)
    result.chiSquared = round(XSquared(text), 4)
    result.letterFrequencies = DecimalFrequency(text)
    result.commonBigrams = GetTextCommonBigrams(text, no_bigrams)
    result.friedmanTest = round(FriedmanTest(text), 4)
    result.entropy = round(Entropy(text), 4)
    result.triEntropy = round(TrigramFitness(text), 4)
    result.cosineFitness = round(TrigramFitness(text), 4)
    result.substitutionFitness = round(SubstitutionFitness(text), 4)
    result.englishFitness = round(SubstitutionFitness(text), 4)
    result.commonMonograms = CommonMonograms(text, no_bigrams)
    result.periodLength = vignere_decoder.GetKeywordLength(text)
    result.length = len(text)
    result.digraphicIndexOC = round(BigraphicIndexOfCoincidence(text), 4)
    return result
