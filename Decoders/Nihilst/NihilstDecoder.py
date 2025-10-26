from Decoders.Nihilst.NihilstResult import *

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
            #print(f"Keyword Length {item[0]}: ")
            for line in item[1]:
                output = ""
                for b in line:
                    output += "X " if b else "- "
                #print(output)
            #print("\n")

"""
    def DisplayComponent(self, component):
        #print(f"Keyword Length {len(component)}: ")
        for line in component:
            output = ""
            for b in line:
                output += "X " if b else "- "
            #print(output)

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
        #print(length)
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
        #print(plaintext)
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

        #print(units_possibilities)
        #print(tens_possibilities)
        #print(keys)

        results = self.GetPossibleResults(ciphertext, keys)
        result = self.GetBestResult(results)

        result.Display(loop)
"""


class NihilistDecoder:
    #     CIPHERTEXT -> TRY_UT -> UT -> KEYLEN  -> TE_COMP -> TENS -> KEYS -> SUBTEXTS -> RESULTS -> RESULT
    #                                -> UN_COMP ->      UNITS      ->

    MAX_KEYWORD_LENGTH = 21
    THRESHOLD = 0.005

    def DisplayComponent(self, component):
        #print(f"Keyword Length {len(component)}: ")
        for line in component:
            output = ""
            for b in line:
                output += "X " if b else "- "
            #print(output)

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
        bestResult = NihilistResult([99, 99, 99], [[99, 99, 99], [98, 98, 98]], "No valid solution.", "No valid solution.")

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
        
        print(ciphertext)

        self.MAX_KEYWORD_LENGTH = 21
        self.MAX_KEYWORD_LENGTH = min(math.floor(len(ciphertext) / 5), self.MAX_KEYWORD_LENGTH)
        
        print(self.MAX_KEYWORD_LENGTH)

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
        
        print(results)

        return self.GetBestResult(results)

    def ReEvaluate(self, result, loop):
        result.plaintext = self.DecryptWithKeys(result.ciphertext, result.keyword)
        result.keyword_len = len(result.keyword)
        result.Display(loop)


