import random

from Utility.Tools import *
from Imports.Ciphers import *


if __name__ == " __main__":
    plaintext = """TO BE OR NOT TO BE THAT IS THE QUESTION WHETHER TIS NOBLER
IN THE MIND TO SUFFER THE SLINGS AND ARROWS OF OUTRAGEOUS
FORTUNE OR TO TAKE ARMS AGAINST A SEA OF TROUBLES AND BY
OPPOSING END THEM TO DIE TO SLEEP NO MORE AND BY A SLEEP TO
SAY WE END THE HEARTACHE AND THE THOUSAND NATURAL SHOCKS
THAT FLESH IS HEIR TO TIS A CONSUMMATION DEVOUTLY TO BE
WISHD TO DIE TO SLEEP TO SLEEP PERCHANCE TO DREAM AY THERES
THE RUB FOR IN THAT SLEEP OF DEATH WHAT DREAMS MAY COME
WUTEVUH"""

    keyword = "ORATIO"

    result = CadenusEncoder(100).GetPracticeProblem(plaintext, keyword)
    print(result.ciphertext)


def DecryptWithKeys(text, permutation, shift, multiple=25):
    key_length = len(permutation)
    length_multiple_requirement = multiple * key_length

    blocks = MakeBlocks(text, length_multiple_requirement)
    permutation = ReducePermutationKeyword(permutation)

    plain = ""

    for block in blocks:
        cosets = MakeCosets(block, key_length)

        permutedCosets = []
        for i in range(key_length):
            permutedCosets.append(cosets[permutation[i]])

        for i, key_char in enumerate(shift):
            permutedCosets[i] = RotateList(permutedCosets[i], key_char)

        plain += Interleave(permutedCosets)

    return plain


if __name__ == "__main__":
    ciphertext = """BETOTOOFIIEEEMLITGOTQRAENIASSUEATSTTFORIBORONNTOROIHAUOSTMT
GREIRFLNSKNAHTSORSRNAFEOEGAHAOTSDHNOUFSBETHWTTENEETADNTSSWR
HUAUEROOSEOTSAAAEYLNAOSKHPDNTAYLMHNDOEITEEEIACHMBTDRNNSHESP
SNHTNFUUWTIHNTORTAAOTLCHPLSATRDTSOBPREDEGETRSHBUOEDOAHESEOE
TNEIHAEIDOEYLTCSAEDMOOLSOTMETOTENETMHDCICFAEOHTREOVLETPNFOS
EAHHURDDEICTSDTRBOWPYHARAEISMARLSMAROTTYAPEAWEHLUVETEIOHADV
MEHEYNATEWUEBSTOENPTS"""

    ciphertext = StringFormat(ciphertext)
    print(DecryptWithKeys(ciphertext, [14, 17, 0, 19, 8], [14, 17, 0, 19, 8]))

    length = 5

    threshold = 0.03

    ###########################

    parent_shift = [0] * length
    parent_permutation = list(range(length))
    best_fitness = SubstitutionFitness(ciphertext)
    best_plaintext = ciphertext

    counter = 0
    while counter < 100000:
        child_shift = parent_shift
        child_permutation = parent_permutation

        swap = random.randint(1, 4)
        if swap == 1:
            change_index = random.randint(0, length - 1)
            child_shift[change_index] = random.randint(0, 25)
        if swap == 2:
            child_shift = KeyWithSwaps(child_shift, 1, False)
        if swap == 3:
            shift_number = random.randint(1, length)
            child_permutation = RotateList(child_permutation, shift_number)
            child_shift = RotateList(child_shift, shift_number)
            child_shift.reverse()
            for i in range(shift_number):
                child_shift[i] -= 1
            child_shift.reverse()
        if swap == 4:
            shift_number = random.randint(1, 25)
            child_shift = [(x + shift_number) % 25 for x in child_shift]

        child_plaintext = DecryptWithKeys(ciphertext, child_permutation, child_shift)
        child_fitness = SubstitutionFitness(child_plaintext)

        if child_fitness < threshold:
            margin = 0
        else:
            margin = ((child_fitness - threshold) ** 2) / 10

        rand = random.randint(1, 20)
        if (child_fitness < best_fitness) or ((child_fitness < best_fitness + margin) and (rand == 20)):
            parent_shift = child_shift
            parent_permutation = child_permutation
            best_fitness = child_fitness
            best_plaintext = child_plaintext
            print(
                f"Counter: {counter} | Key: {parent_shift} | Fitness: {best_fitness} | Text: {best_plaintext[:20]} | Margin {margin}")
            counter = 0
        counter += 1

    plaintext = DecryptWithKeys(ciphertext, parent_permutation, parent_shift)
    print(plaintext)
