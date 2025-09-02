import random

from Utility.Tools import *
import Text.TextGrabber as Text
from Encoders.Ciphers.SubstitutionEncoder import SubstitutionEncoder
from Encoders.Ciphers.AffineEncoder import AffineEncoder
from Decoders.Affine.AffineDecoder import AffineDecoder
from Encoders.Ciphers.VignereEncoder import VignereEncoder
from Decoders.PolySubstitution.PolySubstitutionDecoder import PolySubstitutionDecoder
import math

"""MAX_ITERATIONS = 10000
encoder = SubstitutionEncoder(100)

if __name__ == "":
    ioc = [0] * 2
    entropy = [0] * 2
    cosine = [0] * 2
    xsq = [0] * 2
    trigram = [0] * 2
    iterations = 200
    
    for i in range(iterations):
        english_paragraph = StringFormat(Text.GetParagraph(500))
        random_paragraph = encoder.GetPracticeProblem().ciphertext
        
        ioc[0] += IndexOfCoincidence(english_paragraph); ioc[1] += IndexOfCoincidence(random_paragraph)
        entropy[0] += Entropy(english_paragraph); entropy[1] += Entropy(random_paragraph)
        cosine[0] += CosineFitness(english_paragraph); cosine[1] += CosineFitness(random_paragraph)
        xsq[0] += XSquared(english_paragraph); xsq[1] += XSquared(random_paragraph)
        trigram[0] += TrigramFitness(english_paragraph); trigram[1] += TrigramFitness(random_paragraph)
        
    
    ioc = [f / iterations for f in ioc]
    entropy = [f / iterations for f in entropy]
    cosine = [f / iterations for f in cosine]
    xsq = [f / iterations for f in xsq]
    trigram = [f / iterations for f in trigram]
    
    for metric in [ioc, entropy, cosine, xsq, trigram]:
        print(metric, metric[1]-metric[0])
      
      
def StochasticAlgorithm(text):
    parent = KeyWithSwaps(ALPHABET, 0)
    parent_fitness = SubstitutionFitness(encoder.Encode(text, parent))
    threshold = 0.03
    
    iterations = 0
    for k in range(MAX_ITERATIONS):
        iterations += 1
        child = KeyWithSwaps(parent, random.randint(1, 2))
        child_fitness = SubstitutionFitness(encoder.Encode(text, child))
        
        if child_fitness < parent_fitness:
            parent = child
            parent_fitness = child_fitness
        
        if child_fitness < threshold:
            break
            
    print(f"Solution found in {iterations} iterations:")
    print(encoder.Encode(text, parent))
    
    

if __name__ == "":
    encoder = SubstitutionEncoder(100)
    averages = []
    no_trials = 100
    no_swaps = 26
    for i in range(no_swaps):
        print(f"In Progress... ({i} / 26)")
        total = 0
        for j in range(no_trials):
            plaintext = StringFormat(Text.GetParagraph(100))
            key = KeyWithSwaps(ALPHABET, i)
            ciphertext = encoder.Encode(plaintext, key)
            total += SubstitutionFitness(ciphertext)
        averages.append(total / no_trials)
    
    for average in averages:
        print(average)
    
if __name__ == "":
    for i in range(10):
        problem = encoder.GetPracticeProblem()
        print(problem.ciphertext)
        input("Press Enter to continue...")
        StochasticAlgorithm(problem.ciphertext)
        input("Press Enter to continue...")
        
if __name__ == "":
    ciphertext = encoder.GetPracticeProblem().ciphertext
    print(ciphertext)
    input("press enter to continue...")
    StochasticAlgorithm(ciphertext)
    
if __name__ == "":
    totals = [0, 0]
    for i in range(100):
        text = Text.GetRandomParagraph(1000)
        totals[0] += EnglishFitness(text)
        totals[1] += SubstitutionFitness(text)
    print(totals[0] / 100)
    print(totals[1] / 100)
    
if __name__ == "__main__":
    text = Text.GetRandomParagraph(1000)
    StochasticAlgorithm(text)    """

if __name__ == "__main__":
    encoder = VignereEncoder(100)
    decoder = PolySubstitutionDecoder()
    
    problem = encoder.GetPracticeProblem()
    ciphertext = problem.ciphertext
    keylen = len(problem.keyword)
    print(ciphertext[:50])
    
    plaintext, keys, min_fitness, big_counter = decoder.StochasticHillClimb(ciphertext, keylen, 10000, threshold=0.015)
    print(plaintext)
    print(keys)
    print(min_fitness)
    print(big_counter)
        
        
        
        
    
        
        
        