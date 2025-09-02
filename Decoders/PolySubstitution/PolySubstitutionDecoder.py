import random

from Decoders.Vignere.VignereDecoder import VignereDecoder
from Utility.Tools import *
from Encoders.Ciphers.SubstitutionEncoder import SubstitutionEncoder
from Decoders.Substitution.SubstitutionDecoder import SubstitutionDecoder
from Decoders.PolySubstitution.PolySubstitutionResult import PolySubstitutionResult

class PolySubstitutionDecoder:
    
    vignere_decoder = VignereDecoder()
    substitution_encoder = SubstitutionEncoder(100)
    substitution_decoder = SubstitutionDecoder()
    
    def DecodeWithKeywords(self, ciphertext, keywords):
        length = len(keywords)
        cosets = MakeCosets(ciphertext, length)
        decoded_cosets = []
        for i, coset in enumerate(cosets):
            plaintext = self.substitution_encoder.Encode(coset, keywords[i])
            decoded_cosets.append(plaintext)
        return Interleave(decoded_cosets)

    def StochasticHillClimb(self, ciphertext, length, max_iterations, threshold,
                            initial_temperature=5.0, cooling_rate=0.9995,
                            restart_interval=5000, neighbor_samples=20):
        big_counter = 0

        min_fitness = EnglishFitness(ciphertext)
        min_text = ciphertext
        keys = [KeyWithSwaps(n=26) for _ in range(length)]

        temperature = initial_temperature
        last_improvement = 0  # track when last improvement happened

        while big_counter < max_iterations * length:
            for i in range(length):
                parent = KeyWithSwaps(keys[i], 26)
                new_keys = keys.copy()
                new_keys[i] = parent
                plaintext = self.DecodeWithKeywords(ciphertext, new_keys)
                parent_fitness = EnglishFitness(plaintext)
                little_counter = 0

                while little_counter < max_iterations / 10:
                    # === Best-of-n neighbors step ===
                    best_child = None
                    best_child_fitness = float("inf")
                    for _ in range(neighbor_samples):
                        candidate = KeyWithSwaps(parent, random.randint(0, 5))
                        new_keys = keys.copy()
                        new_keys[i] = candidate
                        plaintext = self.DecodeWithKeywords(ciphertext, new_keys)
                        candidate_fitness = EnglishFitness(plaintext)
                        if candidate_fitness < best_child_fitness:
                            best_child = candidate
                            best_child_fitness = candidate_fitness
                            best_child_plaintext = plaintext

                    # Now we have the best child among the sampled neighbors
                    child = best_child
                    child_fitness = best_child_fitness
                    plaintext = best_child_plaintext

                    # Acceptance rules
                    if child_fitness < parent_fitness:
                        parent = child
                        parent_fitness = child_fitness
                        little_counter = 0
                    else:
                        delta = child_fitness - parent_fitness
                        acceptance_prob = math.exp(-delta / max(temperature, 1e-6))
                        if random.random() < acceptance_prob:
                            parent = child
                            parent_fitness = child_fitness

                    little_counter += 1
                    big_counter += 1
                    temperature = max(temperature * cooling_rate, 1e-4)

                    # Debug logging
                    print(f"Big Counter: {big_counter} | Little Counter: {little_counter} | "
                          f"Fitness: {min_fitness:.4f} | Temp: {temperature:.4f}")

                    # Update global best
                    if child_fitness < min_fitness:
                        min_fitness = child_fitness
                        keys[i] = parent
                        min_text = plaintext
                        last_improvement = big_counter
                        print(f"Iteration {big_counter}: {plaintext[:50]} ")
                        print(f"Keys: {keys[i]}")
                        big_counter = 0
                        temperature = initial_temperature  # reheat after a good improvement

                    # Early stop if close enough to English
                    if min_fitness < threshold:
                        return min_text, keys, min_fitness, big_counter

                    # Random restart if stuck
                    if big_counter - last_improvement > restart_interval:
                        keys[i] = KeyWithSwaps(n=26)  # re-randomize this alphabet
                        print(f"Random restart triggered at {big_counter}")
                        big_counter = 0
                        temperature = initial_temperature
                        break  # break inner loop to restart fresh

        return min_text, keys, min_fitness, big_counter
            
                    
                        
                    
                        
                        
                    
    
    
    def ClimbWithLength(self, ciphertext, length, max_iterations, threshold):
        cosets = MakeCosets(ciphertext, length)
        results = []
        
        for coset in cosets:
            result = self.substitution_decoder.StochasticDecode(coset, max_iterations, threshold)
            results.append(result)
        
        keywords = [key for _, key, _ in results]
        plaintext = Interleave([text for text, _, _ in results])
        iterations = sum([iteration for _, _, iteration in results])
        
        return plaintext, keywords, iterations
        
    
    def Decode(self, ciphertext, max_iterations, threshold):
        ciphertext = StringFormat(ciphertext)
        length = self.vignere_decoder.GetKeywordLength(ciphertext)
        plaintext, keywords, iterations = self.ClimbWithLength(ciphertext, length, max_iterations, threshold)
        result = PolySubstitutionResult(keywords, plaintext, ciphertext, iterations)
        return result
        