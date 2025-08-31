from Utility.Tools import *
from Decoders.Nihilst.NihilstResult import *
import math

"""

    Method Source: https://toebes.com/codebusters/Samples/CodeBusters_Overview.pdf pg. 83, 20.A

    boolean[][]  TRY_UT -> Unit Table Component for specific attempted key length
    UnitTable    UT -> Sorts automatically according to SORT_A

    boolean[][]  UN_COMP -> The Unit Table Component that goes with the KEYLEN
    int[][]        UNITS -> Possible Key Segments, for the units in the key numbers

    boolean[][]  TE_COMP -> Tens Table Component.
    int[][]        TENS -> Possible Key Segments, for the tens in the key numbers

    int          KEYLEN -> Length of Keyword
    int[][]      KEYS -> Possible keys from data.

    String[]     SUBTEXTS -> Possible subtexts from possible keys

    NihilistResult[] RESULTS -> Possible Results. Best selected based on Index Of Coincidence.

    Note: KEYLEN and COMP are packaged as 1 Map.Entry(), ENTRY. Note ENTRY.GetKey = COMP, ENTRY.GetValue = KEYLEN.

    SORT_A:
    1. According to
        # cases that look like the following: false true false | false true true | true true false (ascending)
        + # false
    2. According to associated keyword length (ascending)

"""


class UnitTable:
    table = []

    def __init__(self):
        pass

    def Put(self, component):
        self.table.append((len(component), component))
        self.table = sorted(self.table, key=lambda x: UnitTable.EvaluateComponent(x[1]))

    def GetFirstItem(self):
        return self.table[0]

    def GetValues(self):
        indicies = []
        for index, component in self.table:
            indicies.append(index)
        return indicies

    def GetComponent(self, index):
        for i, component in self.table:
            if i == index:
                return component
        return -1

    @staticmethod
    def EvaluateComponent(component):
        score = 0
        for coset in component:
            for i in range(10):
                prev = (i - 1) % 10
                suc = (i + 1) % 10

                if not coset[i]: score += 1; continue;
                if (not coset[prev]) | (not coset[suc]): score += 1

        return score

    def Display(self):
        for item in self.table:
            print(f"Keyword Length {item[0]}: ")
            for line in item[1]:
                output = ""
                for b in line:
                    output += "X " if b else "- "
                print(output)
            print("\n")

"""
    def DisplayComponent(self, component):
        print(f"Keyword Length {len(component)}: ")
        for line in component:
            output = ""
            for b in line:
                output += "X " if b else "- "
            print(output)

    # Returns TRY_UT, null. Null if table is invalid (see Method Source).
    def TryKeywordLength(self, ciphertext, length):
        table = []
        for _ in range(length):
            table.append([False for i in range(10)])

        cosets = MakeCosets(ciphertext, length, False)

        for i in range(length):
            for x in cosets[i]:
                unit = x % 10
                table[i][unit] = True

            total = sum(table[i])

            if total > 5: return None
        return table

    # Returns UT. Doesn't contain any null tables, only valid ones. Best are first in the map. Gets TRY_UT.
    def GetUnitTable(self, ciphertext):
        table = UnitTable()
        table.table = []

        for i in range(4, self.MAX_KEYWORD_LENGTH):
            component = self.TryKeywordLength(ciphertext, i)
            if component is None:
                continue

            table.Put(component)

        return table

    # Returns KEYLEN & UN_COMP in ENTRY. Gets UT.
    def GetKeyLengthComponent(self, table):
        return table.GetFirstItem()

    # Returns TE_COMP. Takes in KEYLEN.
    def GetTensComponent(self, ciphertext, length):
        table = []
        for _ in range(length):
            table.append([False for i in range(10)])

        cosets = MakeCosets(ciphertext, length, False)

        for i in range(length):
            for x in cosets[i]:
                tens = int(((x - (x % 10)) / 10) % 10)
                table[i][tens] = True

        return table

    # Returns A. UNITS, B. TENS. Given A. UN_COMP, B. TE_COMP
    def GetDigitPossibilities(self, component):
        possibilities = [[] for _ in component]

        for i in range(len(component)):
            minimum, length = GetSpan(component[i])
            options = GetStartingPositions(minimum, length)
            possibilities[i] = options

        return possibilities

    # Returns KEYS
    def GetPossibleKeys(self, units, tens):
        length = len(units)
        print(length)
        possibilities = [[] for _ in range(length)]

        for i in range(length):
            options = []
            for u in units[i]:
                for t in tens[i]:
                    options.append(10 * t + u)
            possibilities[i] = options

        return CartesianProduct(possibilities)

    # Returns PLAINTEXT. Gets plaintext from ciphertext and keys.
    def DecryptWithKeys(self, ciphertext, key):
        length = len(key)
        cosets = MakeCosets(ciphertext, length, False)

        for i in range(length):
            for j in range(len(cosets[i])):
                cosets[i][j] -= key[i]

        plaintext = InterleaveList(cosets)
        print(plaintext)
        output = ""

        for char in plaintext:
            x = int(char % 10)
            y = int((char - x) / 10)

            if (x > 5) | (y > 5):
                output += "j"
                continue
            output += PolybiusDefault[x - 1][y - 1]

        return output

    # Returns RESULTS. Takes in keys and evaluates them.
    def GetPossibleResults(self, ciphertext, keys):
        results = []

        for key in keys:
            plaintext = self.DecryptWithKeys(ciphertext, key)
            result = NihilistResult(key, keys, plaintext, ciphertext)
            results.append(result)

        return results

    # Returns RESULT. Chooses the NihilistResult with the closest IoC to English. Takes in RESULTS.
    def GetBestResult(self, results):
        minDifference = 10
        bestResult = None

        for result in results:
            ioc = IndexOfCoincidence(result.plaintext)
            difference = abs(ioc - ENGLISH_IOC)

            if difference < minDifference:
                minDifference = difference
                bestResult = result

        return bestResult
        
            def Decode(self, ciphertext, loop):
        ciphertext = [int(x) for x in NumberFormat(ciphertext).split(" ")]
        unit_table = self.GetUnitTable(ciphertext)

        unit_lengths = unit_table.GetValues()

        unit_table.Display()

        length, unit_component = self.GetKeyLengthComponent(unit_table)
        tens_component = self.GetTensComponent(ciphertext, length)

        units_possibilities = self.GetDigitPossibilities(unit_component)
        tens_possibilities = self.GetDigitPossibilities(tens_component)

        keys = self.GetPossibleKeys(units_possibilities, tens_possibilities)

        print(units_possibilities)
        print(tens_possibilities)
        print(keys)

        results = self.GetPossibleResults(ciphertext, keys)
        result = self.GetBestResult(results)

        result.Display(loop)
"""


class NihilistDecoder:
    #     CIPHERTEXT -> TRY_UT -> UT -> KEYLEN  -> TE_COMP -> TENS -> KEYS -> SUBTEXTS -> RESULTS -> RESULT
    #                                -> UN_COMP ->      UNITS      ->

    MAX_KEYWORD_LENGTH = 21
    THRESHOLD = 0.003

    def DisplayComponent(self, component):
        print(f"Keyword Length {len(component)}: ")
        for line in component:
            output = ""
            for b in line:
                output += "X " if b else "- "
            print(output)

    def CountUnits(self, coset):
        output = [0 for i in range(10)]
        for c in coset:
            output[c % 10] += 1
        return output

    def TryKeywordLength(self, text, length):
        table = []
        cosets = MakeCosets(text, length, False)
        for i in range(length):
            count = self.CountUnits(cosets[i])
            count = [count[i] != 0 for i in range(10)]
            total = sum(count)

            if total > 5:
                return None

            table.append(count)
        return table

    def MakeUnitTable(self, ciphertext):
        table = UnitTable()

        for i in range(1, self.MAX_KEYWORD_LENGTH):
            component = self.TryKeywordLength(ciphertext, i)
            if component is None: continue
            table.Put(component)

        return table

    def GetTensComponent(self, ciphertext, length):
        table = []
        for _ in range(length):
            table.append([False for i in range(10)])

        cosets = MakeCosets(ciphertext, length, False)

        for i in range(length):
            for x in cosets[i]:
                tens = int(((x - (x % 10)) / 10) % 10)
                table[i][tens] = True

        return table

        # Returns A. UNITS, B. TENS. Given A. UN_COMP, B. TE_COMP

    def GetDigitPossibilities(self, component):
        possibilities = [[] for _ in component]

        for i in range(len(component)):
            minimum, length = GetSpan(component[i])
            options = GetStartingPositions(minimum, length)
            possibilities[i] = options

        return possibilities

    def GetPossibleKeys(self, units, tens):
        length = len(units)
        possibilities = [[] for _ in range(length)]

        for i in range(length):
            options = []
            for u in units[i]:
                for t in tens[i]:
                    options.append(10 * t + u)
            possibilities[i] = options

        return CartesianProduct(possibilities)

    def DecryptWithKeys(self, ciphertext, key):
        length = len(key)
        cosets = MakeCosets(ciphertext, length, False)

        for i in range(length):
            for j in range(len(cosets[i])):
                cosets[i][j] -= key[i]

        plaintext = InterleaveList(cosets)
        output = ""

        for char in plaintext:
            y = int(char % 10)
            x = int((char - y) / 10)

            if (x > 5) | (y > 5):
                return "Please stick to the possible values list. If this is coming up immediately, you probably are not using a Nihilist Cipher. The results of this analysis are 100% conclusive and are the only possible ones in this keyword length which we have decided most likely. If you have a different keyword length, ur on ur own."
            output += PolybiusDefault[x - 1][y - 1]

        return output

    def ValidateTensComponent(self, component):
        for coset in component:
            total = sum(coset)
            if total > 6:
                return False
        return True

    def GetPossibleResults(self, ciphertext, keys):
        results = []

        for key in keys:
            plaintext = self.DecryptWithKeys(ciphertext, key)
            result = NihilistResult(key, keys, plaintext, ciphertext)
            results.append(result)

        return results

    def GetBestResult(self, results):
        minDifference = 10
        bestResult = None

        for result in results:
            ioc = IndexOfCoincidence(result.plaintext)
            difference = abs(ioc - ENGLISH_IOC)

            if difference < minDifference:
                minDifference = difference
                bestResult = result

        return bestResult


    def Decode(self, ciphertext):
        ciphertext = NumberFormat(ciphertext)
        ciphertext = [int(x) for x in ciphertext.split()]

        self.MAX_KEYWORD_LENGTH = 21
        self.MAX_KEYWORD_LENGTH = min(math.floor(len(ciphertext) / 5), self.MAX_KEYWORD_LENGTH)

        table = self.MakeUnitTable(ciphertext)

        results = []
        lengths = table.GetValues()
        validated_lengths = []
        for length in lengths:
            tens_component = self.GetTensComponent(ciphertext, length)

            if not self.ValidateTensComponent(tens_component): continue
            validated_lengths.append(length)

        validated_lengths = RemoveMultiples(validated_lengths)
        print(validated_lengths)

        for length in validated_lengths:
            units_component = table.GetComponent(length)
            tens_component = self.GetTensComponent(ciphertext, length)
            unit_values = self.GetDigitPossibilities(units_component)
            tens_values = self.GetDigitPossibilities(tens_component)

            keys = self.GetPossibleKeys(unit_values, tens_values)

            self.DisplayComponent(tens_component)

            length_results = self.GetPossibleResults(ciphertext, keys)
            results += length_results

        return self.GetBestResult(results)

    def ReEvaluate(self, result, loop):
        result.plaintext = self.DecryptWithKeys(result.ciphertext, result.keyword)
        result.keyword_len = len(result.keyword)
        result.Display(loop)





if __name__ == "__main__":
    NihilistDecoder().Decode("78 38 48 47 67 87 55 30 77 70 64 99 56 39 74 79 54 89 47 27 44 78 65 70 77 50 54 80 58 89 48 49 68 86 65 78 78 38 48 90 96 79 65 47 45 50 87 87 68 68 48 78 54 89 47 38 44 78 57 70 76 60 68 69 54 107 57 37 44 80 58 67 44 58 55 50 87 66 46 28 57 49 58 89 78 26 65 67 98 98 84 49 44 57 86 90 84 49 47 46 86 70 44 49 48 56 64 79 46 39 48 69 88 100 57 48 48 88 54 99 78 30 76 80 78 90 44 60 78 50 77 69 44 49 78 79 78 89 77 68 57 69 65 69 76 26 86 70 86 67 44 59 46 86 75 70 45 58 57 49 65 70 77 28 44 69 57 70 65 26 88 80 86 66 54 36 57 48 78 107 48 58 78 58 58 67 76 39 47 57 58 90 76 39 67 80 66 70 86 26 78 50 86 108 44 70 84 69 57 70 76 49 48 46 88 78 45 70 45 50 67 89 55 59 65 70 96 67 68 26 78 48 54 96 78 26 57 69 87 68 44 49 65 50 54 107 48 66 67 46 88 100 48 49 47 50 57 69 76 26 86 47 86 79 47 37 48 79 78 96 48 49 57 69 78 98 47 30 76 80 78 78 68 47 47 86 84 98 68 26 47 80 86 66 54 36 57 48 54 69 47 50 76 79 94 67 78 58 44 48 88 68 68 48 74 50 77 99 44 60 57 69 65 88 44 37 67 50 88 99 78 50 78 58 58 68 68 48 74 46 87 99 68 49 46 46 86 77 68 59 56 59 84 99 47 30 66 46 65 89 48 60 57 90 58 100 56 30 46 70 76 96 44 59 77 70 86 88 44 47 44 49 68 106 77 60 57 80 55 110 46 50 67 48 58 66 65 39 67 57 54 87 44 58 55 50 55 66 76 50 54 79 88 70 48 47 68 78 67 98 68 49 67 50 54 98 78 50 57 80 55 68 44 58 55 70 96 78 57 47 48 67 78 66 47 39 67 57 78 98 84 49 65 70 54 69 57 49 55 58 54 89 47 47 48 48 54 98 55 50 46 46 86 70 65 30 77 79 75 110 57 49 68 78 57 70 76 60 68 48 54 106 77 30 47 46 76 66 55 30 44 78 86 66 67 37 48 80 66 70 46 26 76 57 78 99 68 60 56 46 88 100 56 30 86 50 54 86 48 59 78 46 77 69 65 39 55 58 88 70 77 60 46 78 54 100 48 59 44 69 57 67 68 69 48 79 96 79 65 47 45 50 54 100 78 38 48 47 78 100 78 50 66 70 64 100 56 30 56 70 75 69 86 38 57 67 58 100 56 30 56 50 54 107 57 30 77 80 78 89 48 59 44 78 58 90 67 60 68 76 78 76 78 38 48 68 84 106 78 38 44 80 56 78 46 50 85 50 86 99 44 49 47 80 54 98 74 26 84 67 67 89 77 50 67 79 75 90 74 56 57 67 98 99 68 60 56 46 88 98 44 39 67 46 77 69 47 30 46 66 96 66 77 38 86 59 75 87 57 49 58 86 86 70 78 38 48 48 54 98 55 50 78 59 58 76 65 50 44 80 95 66 65 67 48 79 78 96 48 49 77 70 88 78 44 60 77 80 78 98 44 37 48 80 54 89 64 59 86 59 75 87 68 67 48 78 64 87 68 68 68 69 84 70 76 39 77 58 54 67 65 30 55 70 78 69 77 28 68 68 76 106 67 39 46 46 88 79 68 49 77 46 88 70 65 30 74 58 78 89 48 26 78 70 64 76 57 28 48 58 78 100 48 47 44 69 57 70 87 28 56 46 77 77 48 59 86 59 88 68 56 27 68 46 86 69 77 29 48 67 54 110 74 66 78 80 67 89 55 30 67 50 76 110 46 26 65 67 87 100 56 58 68 86 65 78 55 39 85 50 88 78 48 48 86 78 78 89 55 49 84 68 55 70 76 59 46 86 88 100 56 30 66 70 64 76 44 28 46 59 57 70 67 60 44 67 75 110 68 58 54 70 86 77 48 60 78 70 57 79 77 28 68 69 77 70 46 60 78 58 58 88 77 50 78 58 54 100 78 38 48 67 67 89 48 28 44 69 77 90 78 27 48 86 87 70 47 26 55 46 67 89 56 26 66 76 58 98 68 36 54 59 56 79 44 47 44 69 57 70 77 56 48 48 67 66 65 47 88 68 67 87 57 60 44 78 98 67 84 59 57 69 58 99 77 27 88 68 54 86 57 49 55 46 88 87 48 26 77 80 78 89 48 60 48 67 58 96 56 50 67 50 56 66 65 47 44 49 54 110 78 50 44 69 58 89 48 48 88 58 58 66 47 57 84 46 86 100 48 58 77 88 66 70 67 70 68 86 65 70 78 60 56 50 76 100 48 47 65 80 66 70 66 70 68 86 66 66 85 30 78 58 58 108 76 50 67 57 77 106 66 27 48 78 56 66 65 47 66 59 75 79 78 26 76 90 78 98 74 50 65 59 56 70 68 36 54 59 56 70 77 26 67 49 76 66 64 30 44 69 78 89 88 48 68 86 87 76 44 47 77 50 86 70 74 50 76 80 87 90 54 36 57 78 58 99 44 39 76 78 54 79 47 59 45 70 76 67 77 39 67 70 64 76 57 28 48 79 54 89 47 27 84 59 75 69 57 49 55 79 94 99 48 29 45 90 88 78 48 30 67 50 76 110 84 49 77 48 86 70 86 60 56 50 58 66 76 56 56 70 77 70 68 36 78 50 75 70 74 38 68 69 58 98 48 28 48 59 95 70 76 59 44 69 57 98 48 48 68 87 58 100 56 30 47 59 54 96 56 58 44 57 76 70 65 30 46 80 86 79 46 39 44 69 87 66 67 29 78 50 75 70 74 38 68 69 58 98 48 56 44 59 86 88 48 49 46 46 77 88 44 46 48 76 78 90 76 28 68 69 77 70 46 60 57 70 77 99 44 49 47 49 54 88 44 37 48 59 77 99 84 47 44 80 67 90 67 59 68 80 66 66 78 28 76 70 87 99 78 26 65 66 54 89 47 50 78 58 58 98 64 39 67 49 87 90 54 30 65 50 56 100 76 39 46 46 75 79 67 60 48 78 64 70 76 30 67 48 58 108 57 47 65 68 54 86 48 28 68 69 95 70 76 59 44 80 67 90 67 59 56 46 86 69 68 58 57 68 84 90 77 59 57 47 75 70 78 50 84 69 57 70 76 59 78 46 77 69 74 66 78 80 66 70 45 26 78 80 58 98 57 30 77 86 77 69 48 58 44 86 88 90 66 26 78 59 56 99 86 39 78 48 66 67 68 26 76 49 87 90 84 60 68 56 56 90 66 48 57 79 87 79 68 49 45 90 57 98 68 56 74 59 77 77 67 26 57 67 87 88 48 60 44 67 64 79 65 39 67 57 87 90 76 28 68 59 77 99 57 49 78 70 88 78 48 28 48 67 75 99 57 36 88 70 94 68 44 49 78 78 58 66 78 38 44 67 64 100 56 30 45 46 88 100 48 58 57 50 87 79 67 60 56 59 87 108 44 70 78 58 58 99 86 39 78 48 66 67 68 26 76 49 96 79 65 47 77 80 78 96 86 50 76 66 67 89 55 26 86 58 78 87 48 60 48 67 58 96 56 50 67 50 87 110 77 60 48 68 56 66 67 27 48 49 67 99 76 66 74 80 58 69 57 36 88 70 94 68 44 49 74 86 88 96 48 58 46 50 77 100 68 36 78 58 58 68 48 47 65 79 67 89 56 26 65 56 88 78 48 27 44 80 88 70 76 39 48 79 78 76 78 38 48 48 58 89 78 58 44 67 55 66 78 60 48 78 98 98 68 50 66 70 94 100 68 36 68 78 57 70 76 27 78 50 75 70 55 58 44 76 66 69 48 47 44 90 88 78 48 60 76 46 77 99 66 39 77 79 67 90 67 26 67 49 57 70 65 39 85 50 86 110 68 36 78 50 75 70 55 58 44 68 87 100 68 30 67 50 76 110 47 30 77 80 67 89 44 60 57 70 77 99 55 26 76 47 75 70 78 30 65 50 65 98 44 48 77 80 78 70 67 30 66 90 57 70 77 60 57 69 54 100 57 50 67 79 87 90 78 38 44 80 54 89 68 60 56 50 86 100 48 47 48 57 86 66 66 68 57 67 75 78 44 67 48 80 78 67 48 59 48 69 88 90 76 26 65 70 77 77 47 39 77 80 54 89 46 30 46 46 75 87 86 39 65 67 66 66 85 30 78 70 55 70 66 26 47 50 87 90 66 30 78 59 76 70 77 39 78 88 67 87 65 27 48 76 78 99 77 39 45 67 58 100 68 29 68 80 66 79 77 27 88 48 66 66 67 37 57 69 65 66 77 39 67 57 75 70 65 30 78 80 58 98 57 49 44 88 78 98 47 36 68 78 58 109 44 48 74 67 58 68 56 26 67 57 67 89 55 48 57 69 67 88 84 48 78 70 76 79 87 39 66 86 76 99 68 60 56 46 88 100 56 30 74 50 86 99 68 49 76 50 56 70 57 67 57 69 65 100 56 30 78 50 75 70 55 58 44 68 96 79 65 47 67 70 88 86 67 50 86 88 66 70 78 38 48 78 76 79 67 39 66 86 76 90 76 48 44 89 67 88 84 48 57 79 76 70 44 49 78 48 88 98 44 49 77 76 78 98 78 26 78 59 78 89 65 39 67 50 87 68 84 60 78 50 75 70 74 38 68 69 58 66 67 29 78 50 75 70 55 58 44 76 66 100 76 26 67 79 76 79 77 59 57 70 77 87 57 49 48 79 57 66 66 26 55 50 67 89 77 66 65 46 88 79 68 49 68 69 84 90 86 30 76 67 67 89 48 59 78 70 56 66 84 59 48 59 77 100 48 58 54 50 86 70 67 28 48 49 76 66 57 47 74 70 87 100 68 36 54 59 56 70 48 48 74 67 78 110 48 30 77 48 54 89 77 30 48 80 78 79 78 60 56 46 88 70 67 30 66 90 76 66 57 47 57 79 54 87 86 26 88 79 57 70 65 26 88 50 57 67 88 50 67 50 57 66 88 50 76 68 78 98 48 60 56 46 88 79 78 39 77 76 94 100 57 49 86 78 78 89 55 59 44 48 74 99 44 49 47 79 78 90 67 30 66 70 88 79 68 49 74 59 56 100 84 58 48 79 84 98 68 40 48 48 88 90 76 50 74 50 86 66 78 50 76 79 56 66 67 58 84 59 77 89 48 68 77 78 58 70 65 59 44 69 57 90 78 38 48 78 58 89 48 48 88 76 86 90 74 26 55 46 77 69 44 36 57 67 76 99 45 70 45 46 57 76 68 28 84 79 67 89 55 59 74 50 58 69 57 49 55 86 84 90 76 59 65 70 96 79 67 37 47 70 96 89 78 38 48 56 67 87 66 26 67 49 55 110 46 26 84 79 67 89 55 36 76 50 85 106 48 49 78 47 86 70 44 46 44 57 58 79 67 60 56 50 64 79 65 48 44 86 57 79 48 49 46 50 87 68 44 49 76 86 67 89 48 49 48 68 98 96 76 50 74 46 65 66 67 29 44 56 67 87 66 59 45 90 54 96 74 47 44 86 57 79 67 37 78 70 57 98 68 68 67 80 66 70 86 50 76 49 87 90 54 60 56 50 87 96 48 26 64 50 86 67 88 28 68 86 65 78 57 49 55 67 78 106 47 47 88 46 77 69 45 70 78 46 75 86 57 49 55 46 77 110 68 49 48 48 54 89 45 58 48 46 74 106 74 26 77 58 78 108 57 49 55 70 64 66 67 30 67 50 76 110 74 58 68 76 54 77 44 49 47 46 64 79 65 48 45 90 84 106 78 60 57 69 65 100 86 50 68 78 88 78 76 30 48 49 78 110 48 49 65 46 86 77 48 48 68 80 66 99 57 49 44 76 54 96 48 58 45 46 65 100 44 46 48 80 66 70 45 26 55 80 78 100 56 30 66 70 95 79 48 59 86 59 88 78 88 50 84 76 94 100 57 60 68 69 88 78 48 36 65 70 78 98 57 49 44 69 58 88 74 60 88 79 58 68 78 39 68 69 78 76 78 38 48 80 66 70 44 60 48 78 54 99 88 50 84 57 78 79 67 26 67 49 75 70 44 67 48 59 88 90 74 30 67 80 66 70 66 50 78 58 87 108 57 47 65 56 75 110 68 66 78 46 77 69 46 47 57 68 55 79 67 60 68 80 66 70 74 58 68 60 58 68 78 50 76 47 58 66 66 59 68 80 66 66 78 60 56 50 64 79 65 48 86 59 75 87 45 30 68 47 87 68 84 58 48 49 55 110 54 47 84 80 88 70 76 39 67 57 87 78 44 29 68 88 87 76 76 26 47 59 78 99 78 26 78 59 78 89 48 49 55 59 77 70 48 58 77 88 67 87 65 36 57 69 57 79 78 57 84 59 88 70 48 26 77 90 88 90 68 67 48 78 76 90 47 66 65 46 88 70 78 58 44 69 87 88 57 59 77 59 78 89 77 50 54 80 54 87 64 59 45 90 84 70 76 59 68 69 87 77 57 67 57 69 65 70 67 30 66 90 84 98 68 56 44 57 54 89 47 26 68 78 67 89 77 60 76 86 56 100 57 50 67 79 87 90 78 38 44 80 88 78 48 70 86 59 75 87 77 50 84 69 57 66 77 39 54 80 66 70 88 68 48 78 58 100 44 47 64 59 77 77 78 38 76 70 94 77 56 26 56 50 54 107 88 28 68 80 88 90 67 27 65 46 77 86 48 60 86 59 88 78 44 48 68 86 88 78 54 66 65 67 78 76 66 26 76 47 75 70 77 39 67 90 78 106 76 50 86 69 54 96 44 58 78 68 58 89 78 27 84 59 75 69 57 49 55 90 78 106 46 26 67 59 77 100 48 58 54 50 86 70 86 39 78 58 86 66 47 39 68 78 58 68 48 56 78 59 78 89 44 60 78 59 76 70 77 68 56 50 77 100 56 30 48 69 58 88 88 68 44 69 88 99 48 67 48 78 98 67 68 29 88 80 78 87 57 59 78 50 77 100 44 46 48 46 77 70 65 30 46 80 86 79 46 47 57 57 66 100 74 47 84 57 78 76 54 60 56 50 58 89 47 50 54 46 77 70 65 30 46 80 86 79 46 47 57 57 66 100 46 50 76 49 88 66 64 30 77 70 76 70 86 39 76 50 78 106 78 50 54 80 66 70 46 50 76 49 54 89 47 60 57 50 67 100 44 28 76 70 87 99 78 68 68 80 58 98 66 39 67 46 75 99 68 36 44 80 96 90 74 58 68 69 65 96 65 66 55 70 86 100 56 58 48 50 88 70 76 48 57 69 54 87 77 50 54 46 64 90 84 58 74 78 78 89 55 56 65 86 65 100 56 30 67 80 54 86 48 39 78 46 86 90 84 49 47 46 77 69 74 66 78 59 88 79 67 60 68 46 87 88 44 49 88 88 54 87 65 26 67 49 64 87 68 50 76 70 94 100 65 30 78 79 54 99 88 50 84 48 54 89 54 39 67 49 58 66 46 38 78 59 76 70 88 50 84 59 77 99 48 58 78 80 66 70 74 47 84 57 67 89 78 50 44 69 58 108 46 39 76 48 94 79 78 70 68 86 96 79 65 47 45 67 78 108 68 66 78 46 64 106 77 30 44 69 57 99 57 47 48 69 56 70 44 47 65 78 54 69 57 50 77 78 94 89 67 39 67 57 78 89 74 50 86 50 86 76 76 50 66 80 66 66 78 28 57 78 56 106 57 60 84 69 88 79 65 26 67 50 96 76 84 59 48 59 87 96 84 60 57 69 57 66 66 26 55 59 77 77 57 49 77 86 75 66 78 39 68 69 78 89 44 49 88 50 75 70 46 60 76 59 56 66 65 30 75 86 67 96 66 30 67 80 88 70 67 29 77 80 78 68 76 30 44 80 58 98 44 29 57 70 67 89 78 30 76 56 58 98 48 49 46 50 67 89 78 38 48 59 76 88 48 29 57 46 88 70 67 30 57 57 66 67 68 58 56 70 78 69 74 26 76 80 67 68 84 47 44 78 75 110 68 49 65 46 86 77 48 37 48 69 58 98 44 60 68 78 87 89 48 50 67 79 67 77 67 59 54 67 94 90 76 30 77 48 58 89 78 47 57 57 66 100 57 49 55 89 86 66 88 48 44 48 66 79 67 30 77 46 77 69 74 50 86 50 86 87 57 49 48 79 67 76 86 50 76 66 76 70 67 28 44 69 57 66 66 26 55 50 67 89 77 66 65 46 88 79 68 49 68 69 54 78 57 37 56 80 58 89 77 39 68 69 75 79 67 30 67 50 54 98 44 49 48 69 58 88 88 26 57 78 64 79 48 47 47 80 66 70 88 68 57 67 75 88 44 46 48 57 86 90 84 49 47 80 78 96 65 26 67 50 86 66 47 39 68 48 78 88 66 66 67 59 56 66 78 39 68 69 87 69 57 36 54 59 56 106 65 60 44 69 57 96 48 58 56 46 84 99 57 48 74 70 87 99 57 27 65 50 57 106 76 39 67 57 75 90 67 37 74 50 86 79 68 29 77 70 64 100 56 30 47 46 98 70 65 30 46 80 86 79 46 56 68 88 58 98 44 60 84 78 55 79 67 30 77 50 75 70 46 60 76 59 56 88 68 60 68 78 87 100 76 26 67 79 64 90 76 48 48 78 87 99 48 30 45 50 64 66 67 29 55 47 88 98 44 49 77 68 67 99 77 39 68 69 75 79 67 30 77 67 67 89 48 59 66 50 77 68 44 49 65 70 78 99 48 49 44 69 57 69 57 58 78 90 67 89 77 66 65 46 88 90 76 59 78 70 56 66 84 59 48 76 78 108 48 58 65 50 54 86 44 37 48 59 88 108 57 47 65 47 58 97 84 39 78 50 58 66 77 70 78 70 78 76 68 58 78 58 58 88 78 50 78 59 58 66 74 39 48 48 58 90 54 67 48 78 98 78 48 26 85 90 87 100 76 39 67 57 87 70 85 30 76 46 75 100 57 48 48 79 55 66 46 46 44 69 57 76 68 58 78 58 55 70 78 68 48 50 77 100 86 50 74 46 86 66 65 47 48 67 88 98 44 49 77 68 67 99 77 39 68 69 75 79 67 30 77 88 67 89 47 39 67 57 67 100 77 30 85 50 86 66 65 60 84 78 77 99 44 58 68 86 77 69 78 38 48 88 67 98 48 30 44 48 66 100 57 48 48 47 58 76 68 58 48 58 54 89 47 60 56 50 87 100 76 39 67 57 87 78 68 66 65 49 55 70 56 30 44 87 67 87 88 59 44 80 94 98 44 60 48 49 96 79 78 38 77 46 75 100 44 49 47 80 66 70 67 29 76 59 58 69 86 38 48 69 67 100 76 26 57 69 87 100 56 30 77 80 86 79 67 37 45 50 56 90 66 30 77 46 56 90 67 29 84 48 88 90 76 26 67 49 54 99 56 50 76 80 56 79 76 28 84 59 88 108 57 47 65 78 58 99 84 47 78 57 58 89 48 58 44 67 67 89 78 30 76 56 58 98 48 49 46 50 96 79 78 38 68 78 65 66 67 39 88 46 88 79 68 49 77 46 77 69 74 58 68 49 94 68 78 39 68 69 54 90 76 37 44 69 67 110 44 60 57 70 77 99 44 49 47 48 78 89 54 30 76 50 77 68 48 59 57 69 87 79 77 60 68 69 57 90 57 49 55 50 95 70 76 70 78 58 67 89 55", None)
