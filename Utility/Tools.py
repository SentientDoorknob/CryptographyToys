import random
import re
import math
from Utility.TrigramFrequencies import *
from Utility.Digram import digram_frequencies, DigramScores

ENGLISH_IOC = 0.0667
ENGLISH_LETTER_FREQ = [0.0817, 0.0150, 0.0278, 0.0425, 0.1272, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.0010, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
MOST_COMMON_BIGRAMS = [("th", 0.0356), ("he", 0.0307), ("in", 0.0243), ("er", 0.0205), ("an", 0.0199), ("re", 0.0185), ("on", 0.0176), ("at", 0.0149), ("en", 0.0145), ("nd", 0.0135), ("ti", 0.0134), ("es", 0.0134), ("or", 0.0128), ("te", 0.0120), ("of", 0.0117), ("ed", 0.0117), ("is", 0.0113), ("it", 0.0112), ("al", 0.0109), ("ar", 0.0107), ("st", 0.0105), ("to", 0.0105), ("nt", 0.0104), ("ng", 0.0095), ("se", 0.0093), ("ha", 0.0093), ("as", 0.0087), ("ou", 0.0087), ("io", 0.0083), ("le", 0.0083), ("ve", 0.0083), ("co", 0.0079), ("me", 0.0079), ("de", 0.0076), ("hi", 0.0076), ("ri", 0.0073), ("ro", 0.0073), ("ic", 0.0070), ("ne", 0.0069), ("ea", 0.0069), ("ra", 0.0069), ("ce", 0.0065)]
MOST_COMMON_MONOGRAMS = [("e", 0.12702), ("t", 0.09056), ("a", 0.08167), ("o", 0.07507), ("i", 0.06966), ("n", 0.06749), ("s", 0.06327), ("h", 0.06094), ("r", 0.05987), ("d", 0.04253), ("l", 0.04025), ("c", 0.02782), ("u", 0.02758), ("m", 0.02406), ("w", 0.02360), ("f", 0.02228), ("g", 0.02015), ("y", 0.01974), ("p", 0.01929), ("b", 0.01492), ("v", 0.00978), ("k", 0.00772), ("j", 0.00153), ("x", 0.00150), ("q", 0.00095), ("z", 0.00074)]

PolybiusDefault = [["a", "b", "c", "d", "e"],
                   ["f", "g", "h", "i", "j"],
                   ["k", "l", "m", "n", "o"],
                   ["p", "q", "r", "s", "t"],
                   ["u", "v", "w", "x", "y"]]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
BIGRAPHIC_EINHEIT = ['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bs', 'bt', 'bu', 'bv', 'bw', 'bx', 'by', 'bz', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq', 'cr', 'cs', 'ct', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do', 'dp', 'dq', 'dr', 'ds', 'dt', 'du', 'dv', 'dw', 'dx', 'dy', 'dz', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el', 'em', 'en', 'eo', 'ep', 'eq', 'er', 'es', 'et', 'eu', 'ev', 'ew', 'ex', 'ey', 'ez', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo', 'fp', 'fq', 'fr', 'fs', 'ft', 'fu', 'fv', 'fw', 'fx', 'fy', 'fz', 'ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gv', 'gw', 'gx', 'gy', 'gz', 'ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl', 'hm', 'hn', 'ho', 'hp', 'hq', 'hr', 'hs', 'ht', 'hu', 'hv', 'hw', 'hx', 'hy', 'hz', 'ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il', 'im', 'in', 'io', 'ip', 'iq', 'ir', 'is', 'it', 'iu', 'iv', 'iw', 'ix', 'iy', 'iz', 'ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl', 'jm', 'jn', 'jo', 'jp', 'jq', 'jr', 'js', 'jt', 'ju', 'jv', 'jw', 'jx', 'jy', 'jz', 'ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl', 'km', 'kn', 'ko', 'kp', 'kq', 'kr', 'ks', 'kt', 'ku', 'kv', 'kw', 'kx', 'ky', 'kz', 'la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll', 'lm', 'ln', 'lo', 'lp', 'lq', 'lr', 'ls', 'lt', 'lu', 'lv', 'lw', 'lx', 'ly', 'lz', 'ma', 'mb', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mi', 'mj', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nb', 'nc', 'nd', 'ne', 'nf', 'ng', 'nh', 'ni', 'nj', 'nk', 'nl', 'nm', 'nn', 'no', 'np', 'nq', 'nr', 'ns', 'nt', 'nu', 'nv', 'nw', 'nx', 'ny', 'nz', 'oa', 'ob', 'oc', 'od', 'oe', 'of', 'og', 'oh', 'oi', 'oj', 'ok', 'ol', 'om', 'on', 'oo', 'op', 'oq', 'or', 'os', 'ot', 'ou', 'ov', 'ow', 'ox', 'oy', 'oz', 'pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph', 'pi', 'pj', 'pk', 'pl', 'pm', 'pn', 'po', 'pp', 'pq', 'pr', 'ps', 'pt', 'pu', 'pv', 'pw', 'px', 'py', 'pz', 'qa', 'qb', 'qc', 'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp', 'qq', 'qr', 'qs', 'qt', 'qu', 'qv', 'qw', 'qx', 'qy', 'qz', 'ra', 'rb', 'rc', 'rd', 're', 'rf', 'rg', 'rh', 'ri', 'rj', 'rk', 'rl', 'rm', 'rn', 'ro', 'rp', 'rq', 'rr', 'rs', 'rt', 'ru', 'rv', 'rw', 'rx', 'ry', 'rz', 'sa', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sp', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'sx', 'sy', 'sz', 'ta', 'tb', 'tc', 'td', 'te', 'tf', 'tg', 'th', 'ti', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tq', 'tr', 'ts', 'tt', 'tu', 'tv', 'tw', 'tx', 'ty', 'tz', 'ua', 'ub', 'uc', 'ud', 'ue', 'uf', 'ug', 'uh', 'ui', 'uj', 'uk', 'ul', 'um', 'un', 'uo', 'up', 'uq', 'ur', 'us', 'ut', 'uu', 'uv', 'uw', 'ux', 'uy', 'uz', 'va', 'vb', 'vc', 'vd', 've', 'vf', 'vg', 'vh', 'vi', 'vj', 'vk', 'vl', 'vm', 'vn', 'vo', 'vp', 'vq', 'vr', 'vs', 'vt', 'vu', 'vv', 'vw', 'vx', 'vy', 'vz', 'wa', 'wb', 'wc', 'wd', 'we', 'wf', 'wg', 'wh', 'wi', 'wj', 'wk', 'wl', 'wm', 'wn', 'wo', 'wp', 'wq', 'wr', 'ws', 'wt', 'wu', 'wv', 'ww', 'wx', 'wy', 'wz', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf', 'xg', 'xh', 'xi', 'xj', 'xk', 'xl', 'xm', 'xn', 'xo', 'xp', 'xq', 'xr', 'xs', 'xt', 'xu', 'xv', 'xw', 'xx', 'xy', 'xz', 'ya', 'yb', 'yc', 'yd', 'ye', 'yf', 'yg', 'yh', 'yi', 'yj', 'yk', 'yl', 'ym', 'yn', 'yo', 'yp', 'yq', 'yr', 'ys', 'yt', 'yu', 'yv', 'yw', 'yx', 'yy', 'yz', 'za', 'zb', 'zc', 'zd', 'ze', 'zf', 'zg', 'zh', 'zi', 'zj', 'zk', 'zl', 'zm', 'zn', 'zo', 'zp', 'zq', 'zr', 'zs', 'zt', 'zu', 'zv', 'zw', 'zx', 'zy', 'zz']

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
DEFAULT = "\033[0m"

def ApplyToLetters(text, func):
    return "".join([func(letter) for letter in text])


def StringFormat(x):
    return re.sub("[^a-zA-Z]", "", x).lower()


def WhitespaceFormat(x):
    return "".join(x.lower().split())


def DigitFormat(x):
    x = re.sub("\n", " ", x)
    return re.sub("[^0-9]", "", x)


def NumberFormat(x):
    cleaned = re.sub(r'\D', ' ', x)
    cleaned = ' '.join(cleaned.split())
    return cleaned


def Index(char):
    return ord(char) - 97


def MakeCosets(text, num, s=True):
    cosets = [[] for _ in range(num)]

    for i in range(len(text)):
        cosets[i % num].append(text[i])

    if s:
        return ["".join(coset) for coset in cosets]
    else:
        return cosets


def AbsoluteFrequency(text):
    output = [0 for i in range(26)]
    for char in text:
        output[Index(char)] += 1
    return output


def DecimalFrequency(text):
    absolutes = AbsoluteFrequency(text)
    output = []

    for freq in absolutes:
        output.append(freq / len(text))
    return output


def IndexOfCoincidence(text):
    length = len(text)
    
    if length < 2: length = 2
    
    length_mult = length * (length - 1)
    absolutes = AbsoluteFrequency(StringFormat(text))

    total = sum([f * (f-1) for f in absolutes])

    return total / length_mult


def BigraphicIndexOfCoincidence(text):
    length = len(text) // 2

    if length < 2: length = 2

    length_mult = length * (length - 1)
    absolutes = AbsoluteBigramFrequency(text, False).values()

    total = sum([f * (f - 1) for f in absolutes])
    
    return total / length_mult


def ShiftLetters(text, by):
    output = ""
    for letter in text:
        output += chr((ord(letter) - 97 + by) % 26 + 97)
    return output


def Interleave(cosets):
    output = ""

    i = 0
    cont = True

    while cont:
        cont = False
        for coset in cosets:
            if i < len(coset):
                output += coset[i]
                cont = True
        i += 1

    return output


def InterleaveList(cosets):
    output = []

    i = 0
    cont = True

    while cont:
        cont = False
        for coset in cosets:
            if i < len(coset):
                output.append(coset[i])
                cont = True
        i += 1

    return output


def ModularInverse(dividend, divisor):
    for x in range(1, divisor):
        if ((dividend % divisor) * (x % divisor)) % divisor == 1:
            return x
    return 1


def ReducePermutationKeyword(keyword):
    indices = list(range(len(keyword)))
    sorted_indices = sorted(indices, key=lambda n: keyword[n])

    keyword = [0 for _ in indices]

    for i in indices:
        keyword[sorted_indices[i]] = i

    return keyword


def SplitBigrams(text, overlap=False):
    digraphs = []

    indices = list(range(len(text)))[:-1:1 if overlap else 2]
    for i in indices:
        digraphs.append("" + text[i] + text[i + 1])

    return digraphs


def XSquared(text):
    observed = DecimalFrequency(text)
    expected = ENGLISH_LETTER_FREQ

    total = 0
    for i in range(26):
        o = observed[i]; e = expected[i]
        total += (o - e) * (o - e) / e

    return total


def GetPolybiusCoordinates(char):
    if char == "z": return 55
    x = (ord(char) - 97) % 5 + 1
    y = (ord(char) - 97) // 5 + 1

    return 10 * y + x


def GetColumn(array, column):
    return [row[column] for row in array]


def GetSpan(component):
    minimum = 10
    maximum = -1

    for i in range(2, 12):
        if not component[i % 10]: continue;
        if i < minimum: minimum = i
        if i > maximum: maximum = i

    span_length = maximum - minimum + 1
    minimum = minimum % 10

    return minimum, span_length


def GetStartingPositions(minimum, length):
    if length >= 5: return [minimum - 1]

    variance = 5 - length
    points = []

    for i in range(variance + 1):
        point = minimum - i - 1
        if point < 2: break;
        points.append(point)

    return points


def CartesianProduct(sets, index=0):
    if index == len(sets):
        return [[]]

    result = []
    for element in sets[index]:
        for rest in CartesianProduct(sets, index + 1):
            result.append([element] + rest)
    return result


def RemoveMultiples(nums):
    result = []
    for i, n in enumerate(nums):
        if all(n % x != 0 for x in result):
            result.append(n)
    return result


def AbsoluteBigramFrequency(text, overlap=True):
    frequencies = {}
    skip = 1 if overlap else 2
    
    for i in range(26):
        for j in range(26):
            frequencies[chr(i + 97) + chr(j + 97)] = 0
            
    #print(frequencies)
    
    for i in range(len(text) - 1)[::skip]:
        char = text[i] + text[i + 1]
        if not char in frequencies.keys(): frequencies[char] = 0
        frequencies[char] += 1
    
    return frequencies


def DecimalBigramFrequency(text):
    absolute_frequencies = AbsoluteBigramFrequency(text)
    decimal_frequencies = {}
    length = len(text)
    
    for key, value in absolute_frequencies.items():
        decimal_frequencies[key] = round(value / length, 4)
    
    return decimal_frequencies     


def GetTextCommonBigrams(text, n):
    bigrams = DecimalBigramFrequency(text)
    sorted_bigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)
    return sorted_bigrams[:n]


def FriedmanTest(text):
    length = len(text)
    ioc = IndexOfCoincidence(text)
    
    top = 0.026 * length
    bottom = (0.065 - ioc) + length * (ioc - 0.038)
    
    return top / bottom


def Entropy(text):
    frequencies = DecimalFrequency(text)
    return -1 * sum([f * math.log(max(f, 0.0000001), 26) for f in frequencies])


def AbsoluteTrigramFrequency(text):
    trigrams = {}
    for i in range(len(text) - 4):
        trigram = text[i] + text[i + 1] + text[i + 2]
        if trigram in trigrams.keys():
            trigrams[trigram] += 1
        else:
            trigrams[trigram] = 1
    return trigrams


def DecimalTrigramFrequency(text):
    trigrams = {}
    absolute_trigrams = AbsoluteTrigramFrequency(text)
    
    for trigram, frequency in absolute_trigrams.items():
        trigrams[trigram] = frequency / len(text)
        
    return trigrams


def MonogramFitness(text):
    return 1 / XSquared(text)
    
    
def TrigramFitness(text):
    decimal_frequencies = DecimalTrigramFrequency(text)
    
    total = 0
    for key, freq in decimal_frequencies.items():
        log = ENGLISH_TRIGRAM_LOGS[key] if key in ENGLISH_TRIGRAM_LOGS.keys() else -7
        total += log * freq
        
    return total
    
        
def CosineFitness(text):
    u = DecimalFrequency(text)
    v = ENGLISH_LETTER_FREQ
    return Dot(u, v) / math.sqrt(Dot(u, u) * Dot(v, v))
    
    
def Dot(u, v):
    return sum([a * b for a, b in zip(u, v)])


def EnglishFitness(text):
    ioc = IndexOfCoincidence(text)
    entropy = Entropy(text)
    cosine = CosineFitness(text)
    xsq = XSquared(text)
    trigram = TrigramFitness(text)
    
    r_ioc = abs(ioc - 0.0654068375027944) / 0.026910270979189257
    r_entropy = abs(entropy - 0.8877498579011024) / 0.10657989939328039
    r_cosine = cosine - 0.9965427197079826 / 0.24454945732808686
    r_xsq = xsq - 0.011894489327752054 / 6.005321227401251
    r_trigram = abs(trigram - -2.338395627210618) / 3.076404251370689
    
    w_ioc = r_ioc * 1
    w_entropy = r_entropy * 1
    w_cosine = r_cosine * 1
    w_xsq = r_xsq * 1
    w_trigram = r_trigram * 1
    
    score = w_ioc + w_entropy + w_cosine + w_xsq + w_trigram
    
    return score


def SubstitutionFitness(text):
    cosine = CosineFitness(text)
    xsq = XSquared(text)
    trigram = TrigramFitness(text)

    r_cosine = (cosine - 0.9965427197079826) / -0.4100328210646499
    r_xsq = (xsq - 0.011894489327752054) / 10.688762622414947
    r_trigram = abs(trigram - -2.338395627210618) / 3.076404251370689

    w_cosine = r_cosine * 1
    w_xsq = r_xsq * 2
    w_trigram = r_trigram * 1

    score = w_cosine + w_xsq + w_trigram

    return score


def KeyWithSwaps(key="abcdefghijklmnopqrstuvwxyz", n=0, s=True):
    key = list(key)
    for i in range(n):
        a, b = random.randint(0, len(key) - 1), random.randint(0, len(key) - 1)
        temp = key[a]
        key[a] = key[b]
        key[b] = temp
    return "".join(key) if s else key
    

def IsValidKey(key):
    if len(key) != 26:
        #print(f"Invalid Key Length: {len(key)}")
        return False
    
    if len(set(key)) != 26:
        #print(f"Duplicate Characters in Key: {key}")
        return False
    
    if any([not 96 < ord(x) < 123 for x in key]):
        #print(f"Non-Alphanumeric: {key}")
        return False
    
    return True


def InvertKey(key):
    output_key = [""] * 26
    
    for i in range(26):
        key_char = key[i]
        output_key[Index(key_char)] = chr(i + 65)
    
    return "".join(output_key).lower()


def CommonMonograms(text, n):
    frequencies = DecimalFrequency(text)
    tuple_frequencies = [(chr(i + 97), round(freq, 4)) for i, freq in enumerate(frequencies)]
    sorted_frequencies = sorted(tuple_frequencies, key=lambda x: x[1], reverse=True)
    return sorted_frequencies[:n]


def BigramIndex(bigram):
    index1 = Index(bigram[0].lower())
    index2 = Index(bigram[1].lower())
    
    return index1 * 26 + index2


def BigramFromIndex(index):
    index1 = index // 26
    index2 = index % 26
    return chr(index1 + ord('a')) + chr(index2 + ord('a'))


def BigraphicKeyWithSwaps(key=None, n=0):
    if key is None:
        key = BIGRAPHIC_EINHEIT
    
    length = len(key) - 1
    
    for i in range(n):
        a, b = random.randint(0, length), random.randint(0, length)
        temp = key[a]
        key[a] = key[b]
        key[b] = temp
        
    return key


def Transpose(text, n):
    cosets = MakeCosets(text, n)
    return "".join(cosets)


def RotateList(l, n):   
    return l[n:] + l[:n]


def MakeBlocks(l, n):
    num_blocks = (len(l) // n) + 1
    blocks = [""] * num_blocks
    
    for i, element in enumerate(l):
        blocks[i // n] += element
    return blocks[:-1]


def RemoveDuplicates(l):
    for item in list(l):
        while l.count(item) > 1:
            l.reverse()
            l.remove(item)
            l.reverse()
    return l


def CountSymbols(s):
    frequencies = {}
    for char in s:
        if char in frequencies.keys():
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def GetSymbolCount(s):
    return len(CountSymbols(s).keys())


def Mean(ints):
    return sum(ints) / len(ints)


def PossibleDigrams(monograms):
    digrams = []
    for a in monograms:
        for b in monograms:
            digrams.append(f"{a}{b}")
            
    return digrams
    
    