from Utility.Tools import *
from Imports.Ciphers import *

length = 500
ciphers = [(VignereEncoder(length), VignereDecoder()), (AffineEncoder(length), AffineDecoder()), 
           (CaesarEncoder(length), VignereDecoder()), (HillEncoder(length), HillDecoder()), 
           (ColumnarEncoder(length), ColumnarDecoder()),(PermutationEncoder(length), PermutationDecoder()), ]

"""if __name__ == " __main__":
    tests = 500
    length = 500
    
    for encoder, decoder in ciphers:
        encoder.length = length
        
        successes = 0
        for _ in range(tests):
            
            problem = encoder.GetPracticeProblem()
            original_plaintext = problem.plaintext
            ciphertext = problem.ciphertext
            
            result = decoder.Decode(ciphertext)
            
            success = StringFormat(result.plaintext) == StringFormat(original_plaintext)
            if success: successes += 1
            else:
                print(StringFormat(result.plaintext))
                print(StringFormat(original_plaintext))
                print(problem.keyword, result.keyword)
                print("\n\n")
            
        print(f"{str(encoder)}: {successes / tests * 100}%\n")
        input()"""
        
if __name__ == "__main__":
    tests = 10
    length = 10

    encoder = NihilistEncoder(length)
    dec = NihilistDecoder()
    
    successes = 0
    for _ in range(tests):
        problem = encoder.GetPracticeProblem()
        cipher = NumberFormat(problem.ciphertext)
        
        plain = NihilistDecoder().Decode(cipher).plaintext
        if abs(IndexOfCoincidence(plain) - ENGLISH_IOC) <= 0.02:
            successes += 1
        else:
            print(cipher)
            print(plain)
            print(problem.keyword)
            print(IndexOfCoincidence(plain))
            print("\n\n")
    
    print(f"{str(encoder)}: {successes / tests * 100}%\n")
        
        