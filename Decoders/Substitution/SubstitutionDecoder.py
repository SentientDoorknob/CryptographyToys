from Utility.Tools import *
from Encoders.Ciphers.SubstitutionEncoder import SubstitutionEncoder
from Decoders.Substitution.SubstitutionResult import SubstitutionResult

stop = False

class SubstitutionDecoder:
    
    encoder = SubstitutionEncoder(100)
    
    def StochasticDecode(self, ciphertext, max_iterations, threshold):
        parent = KeyWithSwaps(ALPHABET, 0)
        _, parent_text, _ = self.encoder.Encode(ciphertext, parent)
        parent_fitness = SubstitutionFitness(parent_text)

        iterations = 0
        for k in range(max_iterations):
            iterations += 1
            child = KeyWithSwaps(parent, random.randint(1, 2))
            _, text, _ = self.encoder.Encode(ciphertext, child)
            child_fitness = SubstitutionFitness(text)
            print(f"Iteration: {iterations}, Fitness: {parent_fitness}, Plain: {parent_text[:20]}")

            if child_fitness < parent_fitness:
                parent = child
                parent_fitness = child_fitness
                parent_text = text

            if child_fitness < threshold:
                break
                
            if stop:
                return None, None, None
        
        return self.encoder.Encode(ciphertext, parent)[1], parent, iterations
    
    
    def Decode(self, ciphertext, max_iterations, threshold):
        text = StringFormat(ciphertext)
        plaintext, key, iterations = self.StochasticDecode(text, max_iterations, threshold)
        if plaintext is None:
            return None
        encoding = InvertKey(key)
        result = SubstitutionResult(key, plaintext, ciphertext, iterations, encoding)
        #print(result.plaintext)
        return result
    
    def ReEvaluate(self, result, loop):
        _, result.plaintext, _ = self.encoder.Encode(StringFormat(result.ciphertext), result.keyword)
        result.encryption = InvertKey(result.keyword)
        result.Display(loop)
        
        