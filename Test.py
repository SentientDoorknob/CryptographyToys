import random

import Text.TextGrabber
from Utility.Tools import *
from Imports.Ciphers import *
from Profiler.Analyser import Analyse
from Utility.LinearAlgebra import LinearAlgebra
import statistics

length = 500
ciphers = [(PermutationEncoder(length), PermutationDecoder()), (VignereEncoder(length), VignereDecoder()), (AffineEncoder(length), AffineDecoder()), 
           (CaesarEncoder(length), VignereDecoder()), (HillEncoder(length), HillDecoder()), 
           (ColumnarEncoder(length), ColumnarDecoder()),]

if __name__ == " __main__":
    tests = 500
    length = 500
    
    for encoder, decoder in ciphers:
        encoder.length = length
        
        successes = 0
        for _ in range(tests):
            print(_)
            
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
        input()

"""
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
        
"""

if __name__ == " __main__":
    pairs = ['6w', 'in', 'fv', 'hj', 'u2', 'on', 'ti', 'a2', 'p2', '56', 'wl', 'hp', '58', '45', 'rd', 'qd', '89', 'hp', '5c', 'fn', 'rf', 'yv', 'co', 'vp', '6w', 'vx', 'on', 'up', 'of', '89', 'hp', 'pv', 'ov', 'vj', 'vp', '3p', 'ey', 'aw', 'pw', 'y8', 'rd', 'np', 'e5', 'cp', 'av', 'fn', '75', 'w6', 'aw', 'by', 'jr', '2u', '4b', '56', 'vz', 'vo', 'yp', '6w', 'in', 'fv', 'rz', 'ey', 'p0', '0p', 'wl', 'hp', '58', '45', 'rd', 'qd', '89', 'ey', 'oa', 'au', '96', 'uy', '2b', 'hr', 'pw', '0e', 'n3', 'rf', 'yv', 'co', 'c2', 'zv', 'zh', 'wp', 'hy', 'it', 'hp', '6a', 'og', 'qd', '2u', 'os', 'co', 'aw', 'nf', 'aw', 'ie', 'bd', 'mp', 'kd', 'v5', 'f9', '8o', 'hp', 'jr', '84', '48', 'hy', 'wv', 'by', 'rh', 'fr', 'ov', 'e5', 'tn', 'av', 'jo', 'yo', 'hz', 'nf', 'nh', 'vp', '98', 'wv', 'w6', 'yb', 'ar', '0e', 'bv', 'dr', '54', 'o8', 'cw', 'uy', 'qd', 'hp', 'ov', 'fv', 'tm', 'zh', '89', 'by', 'vj', 'p0', 'uv', '0p', 'yb', 'ar', 'rj', 'n6', 'nf', '2b', 'wl', 'hb', '5v', 'aw', 'ov', 'tn', 'pm', 'c5', 'bw', 'vp', 'ih', 'fn', 'nf', 'aw', 'hz', 'am', 'pm', 'yd', 'vo', 'nf', 'aw', '0p', 'le', 'n3', 'vf', '5c', 'ac', 'mp', 'n3', 'h3', 'go', '56', '0e', 'bv', 'dr', '56', 'aw', '2e', 'vo', '2b', '75', 'hp', 'fv', '75', 'mp', 'yp', 'a6', 'aw', 'va', 'oe', 'ey', 'n3', 'rz', 'hz', '5c', '89', 'on', 'pm', 'pw', 'cr', 'pm', 'zr', 'c2', '4b', 'pc', '56', 'hz', 'tn', 'yu', 'rb', 'zh', 'am', '5c', 'ac', 'yp', 'c5', 'dr', '2u', 'yx', 'ra', 'no', 'vd', '5u', 'ey', '0b', 'c5', 'vo', '2t', 'hf', 'am', 'ac', 'te', 'tn', 'pw', 'ua', 'ie', 'tm', 'w6', '2h', '56', 'iw', 'ia', 'dr', 'hp', 'jr', 'dy', 'fn', 'oh', '89', 'ey', 'aw', '2t', 'yn', 'ar', 'bx', 'vp', '0e', 'bv', 'dr', 'au', 'fn', 'ra', 'wp', 'de', 'mb', 'tm', 'pw', 'dr', 'ck', 'qd', 'dr', 'oc', 'hn', 'fn', 'e0', 'yu', 'o8', 'vj', '84', '56', 'aw', 'pw', 'pm', 'fv', 'ie', '45', 'ie', 'lc', 'dr', 'ac', 'hp', 'pw', '89', '95', 'vo', 'cw', 'nf', 'va', 'hw', 'yo', 'pm', 'wr', 'au', 'n6', 'r8', '95', 'wk', '2c', 'rd', 'qd', 'rf', 'uy', 'pu', 'ry', 'zh', 'hf', 'am', 'ac', 'n6', 'rj', 'le', 'vo', 'n3', 'rj', 'e5', 'ct', 'yb', 'zh', 'pd', 'b2', 'by', 'rh', '86', 'jh', '8o', 'ch', 'fn', 'xh', 'we', 'hw', 'by', 'co', 'rf', 'oj', 'sa', '8o', '0e', 'yb', 'ar', 'yp', 'rf', 'hy', 'by', '6a', 'ja', 'dr', 'ba', 'pw', 'up', 'oa', 'nz', 'by', 'rb', 'rd', 'hn', 'ov', '58', 'a3', '96', 'qi', 'vo', 'pw', 'ov', 'ie', 'af', 'kv', 'v5', 'vd', 'oc', 'hn', 'fn', 'ey', 'so', 'ey', 'aw', 'ov', 'de', 'o8', '2b', 'va', 'vp', 'of', 'bv', 'pm', 'tn', '89', 'yo', 'hz', 'vo', 'p0', 'jr', 'ac', 'hp', 'oc', 'le', '8o', 'wp', 'vd', '58', 'pz', 'vp', 'w6', 'na', 'dr', 'ik', 'pz', 'vp', '0e', 'bv', 'dr', '56', 'ck', '6a', 'wn', 'rp', 'vo', 'iv', 'yc', 'up', 'w6', 'w6', '2p', 'e5', '0p', 'u5', 'yp', 'vp', 'vi', 'ew', 'vf', 'yp', 'ck', 'hp', 'ov', 'hp', 'ou', 'ya', 'qo', 'ac', 'yd', 'hp', 'dp', 'dl', 'dp', 'ck', 'tn', '56', 'zh', 'yp', 'va', '6a', 'ia', 'hp', 'ov', 'hz', 'fr', 'np', '45', '6a', 'c0', '67', '59', 'tm', 'mt', 'vf', '89', 'hp', 'av', 'au', 'up', 'bv', 'ra', '2p', 'xy', 'fv', 'hp', 'pw', 'ua', 'vo', 'cp', 'ie', '2c', 'qd', 'en', 'od', '0p', 'tb', 'pu', 'py', 'vp', 'cu', 'e2', '46', 'vo', 'bw', 'py', 'vp', 'ca', 'rc', 'u5', 'nz', 'av', 'ay', 'np', 'e5', 'en', 'od', '0p', 'tb', 'pu', 'rp', 'vf', '56', 'h2', 'u2', 'ed', 'rb', 'va', 'n3', 'vf', '5c', '95', 'pc', 'mp', 'ct', 'wl', 'hp', 'ou', '98', 'vo', 'fp', '6w', 'ay', 'ac', 'hp', 'am', 'av', 'xy', 'va', 'hz', 'np', 'wh', 'ay', '98', 'v2', 'hp', 'pc', 'ed', 'pg', 'ar', '58', '98', 'yv', 'ya', 'qo', 'np', 'oe', 'fv', 'yb', 'qd', 'ca', 'uy', '4p', 'ov', 'dr', 'dk', 'aw', '6a', 'p0', 'zr', 'dr', 'bx', 'vp', 'ne', 'hz', 'p3', 'ay', '89', 'dr', '98', 'v2', 'pw', 'y8', 'a6', 'iv', 'fr', 'hz', 'vp', 'up', 'mp', 'iq', '64', 'rb', 'dv', 'pu', 'ya', 'qo', '6a', 'w6', 'bd', '2p', 'yd', 'qd', 'zv', 'yp', 'vf', 'au', 'vp', 'vo', '6a', 'wn', 'vp', 'an', '5u', '6a', 'np', 'e5', 'hp', 'kc', 'vo', 'pw', 'fv', 'yb', 'sa', 'mt', 'av', 'u5', 'by', 'jr', 'ra', 'ed', 'uy', 'ca', 'hw', 'hp', 'pw', 'ey', 'so', 'ey', 'aw', 'ov', 'nz', 'ov', 'au', 'e2', 'av', '98', 'vi', 'ac', 'it', 'ie', 'ae', 'av', 'yb', 'ar', 'yp', 'ku', 'ov', 'h4', 'ay', 'ov', 'it', 'vz', 'th', 'mp', '45', 'of', 'we', 'rj', 'ar', 'no', 'hp', 'ov', 'hp', '6a', '98', 'vi', 'pu', 'vp', 'ro', '5u', 'ki', 'rd', 'uf', 'bw', 'vp', '48', 'ua', 'o8', 'pz', 'np', 'ul', 'ai', 'zv', '84', 'ov', '6a', 'wy', 'yp', 'bv', '6a', 'ck', 'rf', 'uy', 'pu', 'zo', '8o', 'ik', 'ai', '6a', 'bw', 'vp', 'rn', '8o', '75', 'bw', 'yo', 'pm', 'fv', 'h3', 'rn', 'by', 'ph', 'np', 'wp', 'c2', 'ua', 'on', 'pu', 'vp', '98', 'hy', 'wv', 'pw', 'pv', 'oc', 'of', '89', 'hp', 'pw', 'yh', '6w', 'by', 'y8', 'an', 'by', 'ph', 'rb', 'fa', 'au', '96', 'uy', '2b', 'hr', 'oh', 'er', 'yw', 'dr', 'cx', 'nz', 'by', 'p4', 'ay', 'ov', 'cp', 'r8', 'aw', 'hp', 'oc', 'op', '84', 'fv', 'jo', 'ra', 'ht', 'ou', 'ar', 'bw', 'vp', 'yo', 'in', '56', '3v', 'yd', 'hp', 'hp', 'jr', '48', 'ua', 'vi', 'e2', 'fv', '6n', 'on', 'rd', 'qd', 'ey', 'no', 'ty', '2b', 'hr', 'yp', 'vf', 'au', 'np', 'ul', 'ow', 'ie', 'c5', 'ya', 'tm', 'wt', '58', '95', 'ra', 'v2', 'ey', 'fe', 'p0', 'v5', 'yp', 'ey', 'vo', 'va', '2c', 'fv', 'hp', 'ac', 'e0', 'kd', 'pu', 'np', 'ub', 'ey', '0b', 'cp', 'ia', 'va', 'it', 'hp', 'fr', 'au', 'rp', 'vf', 'od', '2c', 'hz', 'vp', 'ie', 'hw', 'o8', '2p', 'as', 'pw', 'y8', 'af', '6a', 'wn', '56', 'bh', 'rb', 'pz', 'vp', 'tr', '6w', 'ed', 'u5', 'n3', 'hz', 'a2', 'ey', 'v2', 'ed', 'rb', 'va', 'nf', 'aw', 'aq', 'ay', 'mp', 'wx', 'oc', 'vz', 'hw', 'rb', 'qa', 'pd', 'mp', 'hp', 'jr', '48', 'ua', 'v2', 'zv', 'yh', '5c', 'od', 'ap', 'yw', 'ca', 'va', 'e5', 'sa', 'o8', 'lu', 'rp', 'vf', 'ua', 'ya', 'qo', 'yp', 'vf', 'oe', '59', 'p2', '2p', 'yd', 'qd', 'hp', 'am', 'ku', 'e0', '4b', '58', '98', 'yv', '98', 'wv', 'ca', 'of', 'ua', 'yd', 'bd', 'mp', 'uk', 'hy', 'ey', 'oy', 'sa', 'mt', 'av', 'u5', 'it', 'hz', '56', 'bh', 'ph', '67', 'dr', 'bk', 'fr', 'by', 'y8', 'af', 'dr', 'rf', 'uy', 'pu', 'rn', 'vp', 'vo', 'ua', 'de', 'hd', 'fv', 'zh', 'np', '45', 'by', 'zv', 'dr', 'ik', 'yv', 'pd', 'b2', 'by', 'rh', '89', '8o', '5u', 'fn', 'wb', 'bo', '2p', '0e', 'yb', 'u5', 'ie', 'ra', '2c', 'de', 'aw', 'rf', 'uy', 'p0', 'hz', '8o', '3v', 'dr', '8o', 'ca', 'hy', 'pr', 'pm', '48', 'yv', 'a6', 'yb', 'ar', 'hz', 'ay', '56', 'hp', 'ov', 'hp', '5c', 'pw', 'ra', 'yb', 'c5', 'de', 'an', '56', 'a3', '98', 'ni', 'yp', 'up', 'bd', 'bh', 'vp', '0u', 'np', 'hn', '56', 'vo', 'ia', 'dr', 'dq', '8o', 'rp', 'nd', 'ua', 'on', 'ac', '8y', 'qd', 'by', 'hp', 'ov', '56', 'vo', 'hp', 'fr', 'au', 'by', 'rb', 'ra', 'yv', 'ik', 'e5', 'oa', 'c5', 'hw', 'tn', 'ay', 'ey', '0b', 'vf', '58', 'yv', 'de', '46', 'ty', '2b', 'hr', 'dr', 'up', 'v2', 'rf', 'az', 'on', '96', 'vo', 'tn', 'b2', 'au', '56', 'vo', 'ca', 'wy', 'de', 'up', 'bw', 'py', 'vp', 'oh', '5e', 'av', 'yb', 'ar', '89', 'ie', 'sa', '2b', 'bu', 'hp', 'ou', 'ya', 'tm', 'bw', 'yv', 'rd', 'yb', 'af', 'up', '6w', 'dr', 'yp', '6n', '56', '48', 'an', 'by', 'ph', 'np', 'hn', '56', '48', 'hw', 'vp', 'rn', 'ey', '0b', 'ct', 'b2', 'w6', 'ya', 'h2', 'wy', 'hw', 'vp', 'yo', 'ay', 'rd', '0e', 'ck', '48', 'jr', 'ar', 'ac', 'it', 'rc', 'p2', 'av', 'u5', '6a', 'wx', 'vo', 'ac', '89', 'ie', 'yv', 'vf', 'hp', 'ov', 'oc', 'nf', 'oy', 'qf', 'dr', 'tn', 'pw', 'ua', 'ia', 'yd', 'hp', 'ey', 'yh', '5e', '56', '2b', 'qd', 'hp', '5c', 'ed', 'rb', 'va', 'nf', 'aw', 'hp', 'oc', 'ny', '8o', 'og', 'qd', 'rj', 'ub', '6a', 'cp', 'wy', 'a3', 'oj', 'uv', 'bh', '6a', 'jn', 'e2', 'pu', 'c2', 'fv', 'c2', '48', 'n3', 'rj', 'tb', 'pu', 'ei', 'ar', 'rc', 'vd', '58', 'yv', 'ik', 'e5', 'oa', 'c5', 'hw', 'rf', 'oj', 'le', 'av', 'wy', 'qd', 'w6', 'qd', 'ov', 'ua', 'on', '56', 'bd', '1b', 'yc', 'bh', 'r8', 'os', '59', 'zv', 'dr', 'bx', '89', 'ed', 'pu', 'vp', 'yh', 'vh', 'np', 'wl', 'yb', 'c5', 'nz', 'vp', 'rd', 'wb', '85', 'fa', 'py', 'vz', 'by', 'zv', 'ct', 'hn', '5c', 'zv', 'wh', '5e', 'ov', 'ry', 'pm', 'bw', 'py', 'vp', 'up', 'le', 'wp', 'yb', 'ar', 'yp', 'vo', 'e5', 'p0', 'ey', 'of', '5u', 'vo', 'hn', 'vp', 'vo', 'ua', 'de', 'ao', 'fv', 'np', '45', 'ca', 'hz', 'dr', 'rn', '5c', 'zv', 'hn', 'vp', 'vo', 'ua', 'de', 'ad', 'ra', 'wb', 'fr', 'ay', 'by', 'rp', 'vh', 'oy', 'qf', '89', 'wy', 'vj', 'er', 'ov', 'rn', '5u', '6a', 'ra', 'yb', 'hp', 'fn', 'cp', 'av', 'hp', 'kc', 'vo', 'pw', 'fv', 'zb', '8r', 'yp', 'ih', 'dr', 'bx', 'rb', 'hf', 'o8', 'cf', 'bu', 'yp', 'by', 'vj', 'ar', 'bm', 'zv', 'y8', 'ap', 'ov', '56', 'wl', 'hp', 'pv', '56', 'hy', '89', 'cp', 'ew', 'hr', 'tn', 'ov', 'au', '56', 'vo', '6n', 'ac', 'it', 'hp', 'pu', 'vt', 'aw', 'ov', '89', 'hp', '59', 'p0', '3h', 'hp', 'pw', 'in', 'cr', '58', 'yv', '0e', 'bv', 'dr', 'fv', 'ua', 'on', 'pm', 'go', 'pu', 'vp', 'vz', 'an', 'rp', 'vf', 'vp', 'pw', 'vo', 'mp', 'fn', 'fv', 'hp', 'pu', '8o', 'vo', 'hw', '89', 'c5', 'bh', 'n6', 'up', 'hy', 'np', 'ub', 'on', 'e5', 'rj', 'zh', 'n6', 'wi', 'ay', 'hw', 'po', 'ey', 'bq', 'o8', 'ge', 'nf', 'aw', 'ar', 'yp', 'hp', 'pc', '0p', 'ca', 'nz', 'rb', 'bv', 'in', 'cr', '58', 'yv', 'ck', 'va', 'no', 'yp', 'of', 'ey', 'ho', 'ay', 'ov', 'jr', 'dr', 'wy', 'vo', 'bu', 'ct', 'yb', 'n2', 'vo', 'rj', 'hz', 'yt', 'mp', '6a', 'wu', '64', 'pd', 'mp', '89', 'bv', '6a', 'xy', 'qd', 'hp', 'dr', 'jq', '98', 'vo', 'e5', 'hi', 'vh', 'ua', 'p0', 'rf', 'hz', '6a', 'bn', 'vc', 'tb', 'ac', 'it', 'hp', 'fr', 'au', 'rp', 'ct', 'b2', 'wl', 'hp', '57', 'ra', 't0', 'ac', 'ck', 'av', 'pd', '2b', 'qd', 'ey', 'v2', 'ed', 'rb', 'va', 'f9', 'o8', 'lu', 'vp', 'pm', 'ca', 'of', '89', 'iq', 'am', '57', '0e', 'hp', '5c', 'pw', 'yu', 'vf', 'vu', '2b', 'w6', 'aw', 'rt', '46', 'yb', 'pw', 'po', 'ey', 'bq', 'yp', 'dp', 'dl', 'dp', 'ck', '6a', 'b0', 'er', 'pm', 'ed', 'pu', 'np', 'xp', 'ra', 't0', 'ac', 'ck', 'ia', 'fv', 'ra', 'ht', 'pm', 'ar', 'bx', 'ey', 'hj', 'vh', 'jr', 'av', 'yh', 'zv', 'up', 'bw', 'a2', 'ey', 'qi', 'av', 'ov', 'pw', 'y8', 'hd', 'rh', 'rp', 'vf', 'tn', 'ay', 'av', 'ht', '59', '8o', '56', 'nz', 'fv', 'wp', 'aw', 'vp', 'vo', 'dr', '0e', 'n3', 'rf', 'yv', 'co', 'by', 'vf', '5c', 'v3', '8o', 'pu', 'np', 'a6', 'al', 'oh', '84', 'oy', 'pw', 'pu', '86', 'ge', 'ra', 't0', 'ac', 'ck', 'hp', 'pw', 'hp', 'ov', '56', 'vo', 'py', 'vp', 'of', 'mp', 'n3', 'vj', 'pm', 'pc', 'no', 'up', 'wn', 'rp', 'np', 'e5', 'yh', 'ai', 'ca', 'hw', 'vp', '46', 'hp', 'ua', 'on', '58', 'rd', 'hf', '56', '78', 'pz', 'vp', 'rb', 'aw', 'vc', 'pw', 'vp', '0e', 'yb', 'uy', '6a', 'nz', 'rp', 'vf', 'ya', 'qo', 'np', 'jn', 'vu', 'np', 'rd', 'sa', 'mt', 'av', 'u5', 'ar', '2u', 'wv', 'bm', 'kc', '58', 'qi', 'am', '5e', 'ov', 'fv', 'wp', 'aw', '2u', 'vt', 'hj', '6a', 'wx', '58', 'qi', 'pc', 'a2', 'p2', 'au', 'pv', 'en', 'fv', 'yb', 'bd', 'bc', 'vu', 'ph', 'p2', '56', 'oa', 'os', 'e2', 'dr', 'wy', '6d', 'pd', 'ey', 'wl', 'hp', '54', 'rz', 'bv', 'p2', 'ki', 'r8', 'e3', 'pw', 'vp', '0e', 'yb', 'de', '3h', 'hv', 'iw', 'ck', 'va', 'no', 'bd', '2t', '6a', 'bw', 'vp', 'vo', 'on', '5c', '6a', 'r8', 'hp', 'ov', 'ih', '6a', 'bv', 'fv', '89', 'mp', 'on', 'rd', 'qd', 'dr', 'tn', 'yu', 'rp', 'yv', '48', 'ua', 'of', 'on', 'fv', 'yb', 'bd', 'bd', '0p', 'up', 'hw', 'n6', 'by', 'dr', 'bx', 'vp', 'yp', 'vu', 'rp', 'oj', 'aw', 'do', 'yp', 'hp', '6n', 'hp', '5c', 'dr', 'yp', '2b', '95', 'vo', 'mp', 'fn', 'dr', 'ik', 'yv', 'os', 'fy', 'av', 'ia', 'v2', '6a', 'zp', 'ed', 'tm', 'yb', 'fv', 'os', 'e2', 'yh', 'dr', 'by', 'rn', 'np', 'so', 'yp', 'rf', 'vh', 'ov', '48', 'dr', 'hn', 'fv', 'am', 'pu', 'vp', '48', 'ua', 'o8', 'as', 'au', 'pm', '5u', 'yh', 'yu', 'p0', '2t', '48', 'ua', 'vo', 'bw', '5u', 'pa', 'p2', 'ki', 'co', 'hz', 'fr', 'rb', 'va', 'p0', 'yx', 'ph', 'ar', '0e', 'oy', 'va', 'of', 'if', 'yv', 'va', 'zr', '6a', 'bw', 'ay', 'on', 'hw', 'vp', '0e', 'n6', 'zo', 'o8', 'lu', 'vp', 'o8', 'ge', 'rf', 'yv', '8o', 'dk', 'rd', 'nf', 'yb', 'ar', 'n6', 'f9', 'ey', 'aw', 'ac', 'yp', '4b', 'ow', 'hp', 'fv', 'e0', 'ov', 'p2', 'oc', 'af', 'ei', 'co', 'hr', 'yp', 'av', '2b', 'bq', 'up', 'a6', 'aw', 'yp', 'n6', 'oa', '6a', 'wn', '56', 'vo', 'hp', 'pm', 'yx', 'ph', 'rp', 'zv', '57', 'am', '54', 'ov', 'nz', 'rp', 'vf', 'if', 'ty', 'yb', 'hz', '87', 'am', '54', 'hp', 'pm', 'e0', '4b', 'by', '6a', 'bw', 'yv', 'rd', 'qd', 'fn', 'hp', 'kc', 'av', 'ov', 'pw', '8o', 'hj', 'kc', 'dr', 'yp', 'hv', 'oa', '48', 'ua', 'oy', 'qd', 'hp', 'av', 'ku', 'zh', 'wp', 'ck', 'dr', 'ey', 'ni', '5e', 'pm', '84', 'c5', 'hw', 'c2', 'zv', 'yb', 'n3', 'vz', '56', 'vo', '2c', 'aw', 'ov', 'yp', 'r8', 'we', 'bd', 'bh', 'vp', '0e', 'bv', 'dr', 'fv', 'on', 'fc', 'zv', 'yp', 'va', '46', 'hy', '89', '6a', 'av', '8o', '2e', 'zv', 'av', 'up', 'ho', 'oy', 'vf', 'yd', 'hp', 'ey', 'hr', 'ey', 'ny', '8o', '76', 'bd', 'bh', 'vp', 'de', 'mb', 'tm', 'pw', 'y8', 'af', 'dr', 'hp', 'au', '8o', '0b', 'ya', 'tm', 'bn', 'en', 'av', '8y', 'le', 'ed', 'ht', 'vh', 'ra', 'yd', 'yb', 'hz', 'c2', '59', '8o', 'c5', 'yp', 'oj', 'rd', 'fp', '6a', 'jn', 'wp', 'aw', 'fn', 'yw', '5v', 'h0', 'go', 'pu', 'vp', '0e', 'bv', 'dr', 'fv', 'ua', 'on', '5c', '8o', 'wp', '0p', 'aw', 'hp', 'pu', 'c2', 'au', 'b2', 'mb', 'e2', '59', '8o', 'r8', 'we', 'rj', 'hp', 'fn', '98', 'v2', 'pu', 'fr', 'up', 'ab', 'ay', 'sa', 'o8', '2u', 'ey', 'n2', 'o8', 'mp', 'nz', 'by', 'ph', 'np', 'yb', 'v0', 'dr', 'iw', 'ey', 'cv', 'hz', '98', 'vo', 'e5', 'hi', '56', 'mp', 'hy', 'yp', 'hp', 'fr', 'au', 'rp', '2c', 'bq', 'wl', 'wp', '75', 'r8', 'yv', '4b', 'ed', 'oc', 'hw', 'vp', '2b', 'bq', 'hp', 'ey', 'vf', 'yd', 'hp', 'ey', 'wh', 'au', 'c5', 'lc', 'ov', 'rf', 'yv', '2c', 'n3', 'rj', 'ar', 'yd', 'bd', '0b', 'co', '6a', 'jn', 'ay', 'b2', 'bc', '6a', 'ry', 'ad', 'ra', 'u5', 'hw', 'nz', 'rp', 'vf', '2b', 'e5', 'v3', 'ow', 'cp', 'nf', 'e5', 'wt', 'r8', 'yv', 'u5', 'fn', 'pm', 'fv', 'nz', '8o', '79', '8o', 'p0', '2b', 'zh', '48', 'ua', 'hy', 'vp', '0e', 'bv', 'dr', 'pv', 'fn', 'cp', 'av', 'wv', 'pd', 'mp', 'yp', 'up', 'bd', 'mt', 'hz', 'vp', 'ez', 'hv', 'vo', '89', 'ey', 'o8', 'qi', '6a', 'jr', 'pw', 'y8', 'rd', 'af', 'up', '6w', 'ua', 'cv', 'hz', 'ie', 'hw', 'dr', 'v5', 'yp', 'ct', 'b2', 'wy', 'zp', '8o', 'ey', 'of', 'pm', 'e5', 'rf', 'va', 'w6', 'wo', 'wp', 'yb', 'c5', 'dy', 'jr', 'rt', 'ey', 'p0', 'mp', 'e5', 'or', '98', 'hy', 'wv', 'oc', 'hw', 'np', 'ub', 'vy', 'uy', 'p0', 'ya', 'qo']
    replacements = {
        "in": "DR",
        "ni": "RD",
        "hp": "TH",
        "vp": "HE",
        "pv": "EH",
        "eh": "PV",
        "he": "VP",
        
        "dr": "IN",
    }
    
    replacer = replacements.get
    replaced_pairs = [replacer(n, n) for n in pairs]
    print("".join(replaced_pairs))
    
if __name__ == " __main__":
    tests = 500
    results = []
    encoder = HillEncoder(100)
    for i in range(tests):
        print(i)
        text = encoder.GetPracticeProblem().ciphertext
        analysis = Analyse(StringFormat(text), 10)
        results.append(list(analysis)[0])
        
    stats = ["IOC", "DIOC", "FMT", "X2", "E", "3E", "F", "SF"]
    for i in range(len(results[0])):
        stat = LinearAlgebra.GetColumn(results, i)
        mean = round(Mean(stat), 5); std = round(statistics.stdev(stat), 5); SE = round(std * 1.96, 5)
        print(f"Mean: {mean}")
        print(f"Std: {std}")
        print(f"{stats[i]}: {mean} +- {SE} (95% Cl) ({round(SE/mean * 100, 2)}%)\n")

def GetMissingPairs(cipher):
    cipher = WhitespaceFormat(cipher)
    digrams = SplitBigrams(cipher, overlap=True)
    digram_list = RemoveDuplicates(digrams)
    digram_list.sort()
    
    monogram_list = RemoveDuplicates(list(cipher))
    possible_digrams = PossibleDigrams(monogram_list)
    possible_digrams.sort()
    
    difference = set(possible_digrams) - set(digram_list)
    return list(difference)


def GetRowsColumns(digrams, monograms):
    rows = [[] for _ in monograms]
    cols = [[] for _ in monograms]
    indices = GetMonogramsDictionary(monograms)
    
    for missing in digrams:
        first = indices[missing[0]]
        last = indices[missing[1]]
        
        rows[first].append(missing)
        cols[last].append(missing)
    
    return rows, cols
        
    
    
def GetMonogramsDictionary(monograms):
    dictionary = {}
    for i, mono in enumerate(monograms):
        dictionary[mono] = i
    return dictionary
    
    
def GetKeywordDigrams(rows, cols, chars):
    keyword_digrams = []
    
    for row in rows:
        if len(row) == chars - 27:
            keyword_digrams += row
    
    for col in cols:
        if len(col) == chars - 27:
            keyword_digrams += col
    
    return keyword_digrams


def GetBannedLetters(iteration_digrams):
    firsts = []
    lasts = []
    
    for digram in iteration_digrams:
        firsts.append(digram[0])
        lasts.append(digram[1])
    
    firsts_count = CountSymbols(firsts)
    firsts = [key if value >= chars - 27 else "" for (key, value) in firsts_count.items()]
    
    lasts_count = CountSymbols(lasts)
    lasts = [key if value >= chars - 27 else "" for (key, value) in lasts_count.items()]
        
    return firsts, lasts


def DecryptWithKeyword(ciphertext, keyword):
    alphabet_pointer = 0
    keyword_pointer = 0
    
    keyword_len = len(keyword)
    indices = GetMonogramsDictionary(keyword)
    output = ""
    
    for char in ciphertext:
        index = indices[char]
        difference = (index - keyword_pointer) % keyword_len
        keyword_pointer = index
        alphabet_pointer = (alphabet_pointer + difference) % 26
        output += chr(alphabet_pointer + ord("a"))
    
    return output
        
colors = {0: RED,
          1: YELLOW,
          2: GREEN}

def DisplayGrid(grid):
    for row in grid:
        row_string=""  
        for element in row:
            color = colors[element]
            row_string += f"{color}■"
        print(row_string)
        print(DEFAULT)
    


if __name__ == "__main__":
    ciphertext = WhitespaceFormat(input("Enter Ciphertext: ").lower())
    #ciphertext = WhitespaceFormat("JEY@VHRIECWIBIRMBSVECN*LOTHSDIZ*DLPAF*LHUN@XCFXLACYUTHBPTCTKVDENVWEXBVKMVGK#WG*GJVYSI@WAHOMY@YDZQ#JTERJBLHMRBQCXGUAMUBHAPZG@AV#WSPDINPX#HEKEHVLSQID#HVLV@WJZMUHYIMTCWH@CXKVDYOWUEQZGRN#CA#QVECN*ISCVBL@FME#AWOA#TZVMPOZR*CHXKICFSEHXZL@WELWKVW#W@SYOQV*HPIPQAFTXGJV*#MDHVSWLXLU@PHNKIJPBPXPZDJOTIXLRD#HCEIZAOJEBGSOBOXFYPOMERWYSTFMKXRLYSP#@PBZQIB*B#GL*IJXGBVE*QYRSAXYJCGQGWOWSWEO#YUAHVNFSA#HDPQFMRG*DHSKPGPIXGXLGERSCNF*SATJWNHEWXJPJFSI@CUR*VFKQXLQ*#IJUZBCWDHLXSMTJUXFSQRI#FUPM*BMAXYPQOBUZNCLSMROPRW@WJYAWRGTLPG@RIYUCBYN#DXFIWUXOYKN#BOXCVOTHUDOIN#DQSDS@AHZLVIUNG*GHYLBPGUEDUEYMANSDFZRSQIE#Z@BOF*MDR#BXBITBYJSDSHZ#PXUNTRLJOZBCQCLBCFLWZKW#IQEIAWRLUFR*BCBLENRKN*NX@SMA#VWK@IJ*TEJBO@DTFODY@DYRAVYNHZF*NQYFIJY#FGQR#XQWEJPQCBJD*NGS@U#HMOADZWXC@QTXGUTYZ#TWN*VRK*MEFCNQYHLYRGBN#*UBXJOJEHKQVAFXQA#*W*K@PX#*BEMXHBRKGLBLFWSMEWKRVEOZIBQS#MDV#IYS#D@HWEHETUZRB*@DX*XQBKNWKEADIJAY@WNGESGMOBCN#*BXFTCMBXLBIAORIU@XZPLD*EQGJRLGBQZBPQU@DZCTCTKVIPRV#QZSJWBUX*VCP@V*FHBI*PCWX@RJN@LOD@WJDTX@JZBPQW*BJSXAVNWSMEW#QZK#PKIPQAYN#MK*OIN#DLYBKWRQIRXFKWPJT*HJSDLWH#IBWNLKUMNBGIPXTYQT#MYFCMAHQTSDMG#OH*@DPOXFKXKPBLJFSVHRCDYD@GOBVKMCAIPED@RVENPVA#@AFEA#LZ*N*@WXUTRSHQZKAT@QYJETBRSIXZUVGN@*GQRWF*TCDSCSFCJAFZSIAILVGPOTZRJBV#VN*#SCUAOFULUBIJQ@WOIUFUWSFXKFJCJONZDRNYNKYKCJE#ALQSXJKSHTHURK*VLWSCNFOR#*MPT*@BCUVRHXYP*NOINCUHD#P#IJPRJBLMPDNW*NSTBUH#CJZV@RLB#QVCIPF*TKZDSDNIESDSYZKNO@TP#LQG*OHMU#SNQ*JR@CZENOIUIL*OP#PAFJEFXJMSM#YBDOFCLGZJUO*HZ*MWXCLQGVX*BHXT@Q*JRK*BRL@SCKZTGJOTUNIPXAERSILVSVWJRUYNRNLQGWUT@DJ#WCSKNLDLNDGNEIAXYRVKGAIPQAHEKGEHPHY@LMVSIMUFGOXIUQ*#*UTMC*HLNL@BROKRZQJRGJFRK*EDGKTSD#MDPDNFRTYQVLVNFLFTB#CMXQDMGAZMNCNFOQJACAUKYVYIM#BVMFMKTFJACWP#MFXMAHTZ#J#QCSKGLAGMXTIUBLWOG#MHCMCPOS#MDWIET#FIKEFK@XULTYGUTYKCQCSG@MZETUZRSLXKJQVOPBIPXKNSGRUVA#FIP@JMRZT#SY*WX*OMU#SNWH@CXJZUGVPEIAPRQ#OZGLETLRHXYEGHRNY*AHEMRZCFCILRJBVXMNCMLBJSDITRAMEMUYBFWZSEGCOUVP*#MCBRK#PH@JVACLMY@YAWYA*FRGUGKIPNYDMZTRUWCDYD#QZHKR#IRG@AJLAMYVPYRXINRCNOVDWI*PZFXQZMFUXGVDKFULHZ@QJYABTFGNEGKRJPDRHVFIZDJNXAWRJZIDXOPYASBQYKMLPMGNBRKVIBQWKIBVMPKSMCBFJPO#YF@LFTLYHMUN@QKJPVOEBPIFSKNLDYHOIDWNOVOPGEZ*AOTV*J@RFXEHEMRVDR#J*FYG@#JPQJXZEGLIR@#ZGLWRTBGB#S#WOSNPFVYCMUNRMNFL*KMPZDG*QK#QCXGNLDENOIUDZARHJCUBEOZJPJFYTZ@TYLHTAWQOFNOQUPLITEAYVM@GQE*NLDMOYKN@SYA#NC@*EDQ#QOTHJNSNY@QFOUGMZ#P@WJDTX@JDJWKE*RKUCXLUZT*LPTUIQZGI*BLJLO#OY@SXUIVSIU@AHYZTW*BQIBCZBDVSHTKBDQGSMKH#DX@SYOQGESQVAYOZCUP@DZNGRTRZAWJQL@JGWQDJC*B*GYCZEKVIFPANBILZAZBXRTUHMENXG*DETZFN@AHPTWNFEADPXDMXNULHZH#ABMEJNCN@SYA#SKBY#IQ@E*VLFVY*RJAHVMUGKNK@TPOPJXPXY#AMSHTARLXRIMTPWRIQE*ANOQLKPHWOWKTLSCSADZCMCXF@YZAZ#DXLI*GSHZDISNE@UALAON#P@BQWKIYAUNEBGYKRLSVFK*@CVD*ALGWR@XPZATHZE#J#DLPEGSVHRCIDJV@ATOIR#FSPYKGEQYLTSCVB*DFMDCOQUBO*R@CL*AWCZBDJOYEJ*RFWLFVLNHQYEIACAQGABLXACVFKNIAHRYGVCWOQLTYGYHKRC@Q@STFVO*LGNEWOALOTKJPZTBOISXUIK@VLEYGVBWPTFHRMWFLMGTB*DH#ZKW#JRQJQKBIV#JPHIWOWDJCVHPLIDLSISA*NEIUPZDGRGTBP#*U@DZCGSMKVIR*ALVGMZTIQ@EN*SJYVKXISDWALWQAHJSRJMVSBM@ECUXHAVYNKDPEIAQIBX@WOI*CBPJMER#YVKFX@RJY#YPDHNKIUJODGTMKJWRDHUKXKXLENCN@S#QZCJWBUIPKBCBWXSDJMUHXBSQIDZIDJ#ADIULJFUTGJMZ@QJ@SMAN#CLHQF@GYTMXHI*LQ#CBORNBDYJACLMZUZNKX*BYMSMK#SVRGZL@ZEOKHSGINFEQZGRMZTI*TPV#UPYFHLQ#OPHZWRIUIRJBG#J#NF@UCBKUCKIYEOTGNZV#MDWDFXET@M*NTXY#I*FWEMVSIMUFHOW*VWLQTEADZPOHQZ#JRCNCLFQRGSBYHCGWZBNTUXYCOQVUKFKTPQDTWY@M*MNWKTCKZEHTSCUAJZADZQH#*STXEMENEHNSDVDKCNFHZARVEOZGLQTCBOZ@FVYAMFWATJFZ#*IJ*J#W@BXZ#DJWS@QWDHCFLESUXFSFQLYOZI*HXK")
    chars = GetSymbolCount(ciphertext)
    missing_digrams = GetMissingPairs(ciphertext)
    monogram_list = RemoveDuplicates(list(ciphertext))

    missing_no_doubles = list(filter(lambda x: x[0] != x[1], missing_digrams))
    missing_swapped = ["" + x[1] + x[0] for x in missing_no_doubles]
    missing_swapped.sort()
    
    monograms = RemoveDuplicates(list(ciphertext))
    monograms.sort()
    indices = GetMonogramsDictionary(monograms)
    
    table = []
    for i in monograms:
        row = []
        for j in monograms:
            digram = "" + i + j
            row.append(int(digram in missing_swapped))
        table.append(row)
    
    previous_table = []
    for i in range(5):
        previous_table = table.copy()
        
        # first, change 1s into 2s in the rows
        for j in range(chars):
            row = table[j]
            missing_count = sum([x != 0 for x in row])
            if missing_count == chars - 27:
                table[j] = [2 if x != 0 else 0 for x in row]
        
        # and then the columns
        for j in range(chars):
            column = [table[k][j] for k in range(chars)]
            missing_count = sum([x != 0 for x in column])
            if missing_count == chars - 27:
                for k in range(chars):
                    if table[k][j] == 0: continue;
                    table[k][j] = 2
                    
        # then change the 1s to 0s
        for j in range(chars):
            row = table[j]
            keyword_count = sum([x == 2 for x in row])
            if keyword_count == chars - 27:
                table[j] = [0 if x != 2 else 2 for x in row]
        
        # same for the columns
        for j in range(chars):
            column = [table[k][j] for k in range(chars)]
            keyword_count = sum([x == 2 for x in column])
            if keyword_count == chars - 27:
                for k in range(chars):
                    if table[k][j] == 2: continue;
                    table[k][j] = 0
        
        DisplayGrid(table)
        
        if table == previous_table:
            break

        input()

    reverse_indices = {v: k for k, v in indices.items()}
    
    digrams = []
    
    for i in range(chars):
        for j in range(chars):
            if table[i][j] != 2: continue
            digram = "" + reverse_indices[i] + reverse_indices[j]
            digrams.append(digram)
            
    digrams.sort()
    
    print(", ".join(digrams))
    
    keyword = WhitespaceFormat(input("\nKeyword: "))

    best_fitness = 10
    best_plaintext = ""

    for i in range(len(keyword)):
        rotated = RotateList(keyword, i)
        plaintext = DecryptWithKeyword(ciphertext, rotated)
        fitness = abs(IndexOfCoincidence(plaintext) - ENGLISH_IOC)
        print(f"{i} | Plaintext: {plaintext[:20]} | Keyword: {rotated} | Fitness: {fitness}")

        if fitness < best_fitness:
            best_fitness = fitness
            best_plaintext = plaintext

    print("\n\n\n")
    print(best_plaintext)
            

if __name__ == " __main__":
    ciphertext = WhitespaceFormat(input("Enter Ciphertext: ").lower())
    # ciphertext = WhitespaceFormat("XAYIHVBS#URMXE@#WBQPSTGXECXCXPA@OCATLXVBEQSZYB@DTAJSNEKGJDVWEAXA@GBNGQWJQXOJEGPXJLFXFESFMWDOWEKEJFPWE@CABSYUWSKOLZDMH#BIBYTJQYUECVAUEOCSPKWLGM@HIEWNEJKCUBSXMSEQVALMNTUBSNBMD#OJEQGADBPGYPHYQJVHBHIBTDKTAPCEUMI#WEHNGZIDVQXZENWAQBPFHJKMSYOBUORLGNBLZ@#QAWPRIEOVY#@RVYUFCHO@UZJ#DVUNAT#NF@UPXKOPYRSZ@STJHKNSMPRDVXTGEKITAPLUEJ#OVR#SUPJPZKGNGDWCXIPJDIXCPBYOQMSLZUJVNXED#QG#WENUGCN@OFEPATLMPDWLCDEOATAP@D#Z#CFORQLUZPXQ#ZGOKTA@NKMPG#MQLZUJVNB@ADBNALQ@E@KLND#XUF@BL#E@GOBHDA@DTAGXPXIYUVBCYOJ@TQD#WDLIO#NJKB#TDRUZRNG@H#JW#PSE@NRD#XUSLHZSRNXSDXZGKIJEUYXCPVOMHGHSLNULRZPU#UNO@EGEAPEXUFWEACWJYIEMLHJXNOWLIQYXKVXV#GRCMPYKOJDP@DJZGVPOVUBIQGAZIHUYX@RLWBSL@DSGTBEV#PSKEDLGRLORQYVJQWBGBZMDAWCUQ#IKET@PISD@QPVSZGTLTDZODTUO#MEKO@FXOMXCOGZIDVUNAXKRENOQ@FHVAW@UIVPSKGJVRNGQVMDJYBPQBQ@FHOMSFECWORYQSZLMK#ZFPSIJQCEHXSEDHNJQJGZOBPSBQMGUJOMSFECWORYQSZLMK#ZFPSIJQCEHXUJ@MHMPAEGBNXEIDUWCDK#OQYXKMSIVOPBZKQDRGWZSHBYTAPLXB@CSF@SMAYMEJPTHJWGNBYN#UCZMBL#WCSMTGYJOUBHJQZF#ILIESECK@FXIVRXMSENJGQJQDVXECSJU#UKSPAUFBOYVJVJMRVJ#BWCUQKXEJPA@ELVJS#QR@VSEASOGUIMCGDEUYXVYJYLNETQEZO@PQRO#NKMXZOSVASNKLZJFAPWCE#FJVGMKMXDZ@RXMSNSMJNB@XB#JEMNDI@YSKWAP@SRU@H#JABHNQEOLEDASYTCPYOSGMIVGOJQAKUCLXJRNUCPAIHVBDU@LMR#OTLGIZUF#KGXNRDLUMIDZLCOBGZIJHGCYPEGTJ@DUAVAVH#MJRJEYQDRGLHXT#BVF@KSREJCXC@RV#RLGBQNBYTAPDNDKMXSLHUJHKHJBDGIUNTWBV#KTAJVGMK@AUYFZSNOGKRHBTXUJNKDT@JRFEUMIHOBXAEILWTCZSJ#KTAPGIFI@GD@FS#VZLZGJBTCXB#JEMNDUPKXEVL#E#MDWDGHIEWTAPGAZVR#SUGL#EYSWTBI#JZFAVFV@N@R@FSFPJOWJ@ILMIXVZOPBPS@PA@#KBSZ@GPELOROXOHYNEHTJZ@T#J@TPKVZDBPD@OJHEJDHDGQEAWGNBJ@OPCMKBR#IVSCOHYQJUGQ#XZKDGEGXGAZVR#SUXAEYGZIULT#XNXBPJNFUI#UTGLGKOYBLJWMKDFJWBVDRE@FHVYBLSCSZSNK@XHQDEAGNBTJDVZUZF#EUVYPKBSDJXAGAYSLUZG#VIAOHESYJT#HIWOXBCLVQNR@AXUXZNPBRQ@XFHIEWDA@QUDHIXYFZS#JYSPKBDHJSNOACE@KECUIHVYDNHVJDWXHMKDYPGEN@FHJBEVCXUOELYJWMKDTETDSAUCUIECXF@CXPHSZLV#KVUXBJ#EKPKDHLH#PX#TGWTK#HBLXECTJO@VZSVAWQJAUSZKXHSIJOZF#EW@UNKP#XQJUJEYLMNPSWIWBUSPFJUBDVZVFTXCFEGWP@SNBMDWBC#QNPHOBJRTBPUZJHCGQJBZ#DTQYXCKMXDGRMPYJRLRNG@DJZVLICVHEJKPAVF@EM#VYQDUBDXUJWBYDUGYXFCOFEBLGJHUYQJHLT@DTETPRI@PJFC@VF@RVXAHUY@WQEUGWCJ@EIAGVB@AIDORQYOQZLGMLVQXYXTXBQYNRDJ@BZ#FZSY@LZOTLMDAPILIPYUI@HBFSR#RVAV@L#OMKVUZENUAQBPFHDIVXDJSUYFOROSXMATLGXPZ@DSCLUXUIMPKECUGTLRXSTYGZIF#PEWPIFYGOIJVAWDVL#UZPOWDLHEXZT#EQLXCZDJUVCOPBHYMBZBZHXGEUGPNDW@HSE@MXJRBSRNDGZH#JQCPE#SUIMNDKVEXUFCPTLDHMB@V@GW#UAPXNSZPGSAYPVHYXJWMLFZF#@Y@#CUZI#ACVBSMAYQJVUGQMDXBPECUQ#NJVXVGBCP@LIUWSZYXTQYUJ@LXCVCWOUZT#IZJBNYSBDIPSXCZTXLEMNYQJVLIEANOKEBQYXFCXYVQWPDOALM#NGTJFPYBLIPGCKMJDWEALHPHOROVGHIEWDYJNDUZSYOS#DLXMAJHJL#OMK#CDECD#KTFPDXCOMPVHC@YSMOKSZRXLTHJOE#UPKRUCGLUXBEAORXPHEQSHRXMKL@IS@TDUG#PCDIVAI#WZ@BMJ@LSROUKL@I@LOXQTJUGCX@SR@CPYTLQDUBZDEVLI@FHFLFAEBSTPY#UK@OWJLTDJZF#QP@LUEHXVMCWJYQJNB@#WGBCTQGKUGLPFXOASABRZ@KMKDZTXSTAPYXJFXAEBSNGZIB@IBFPSIPQUIJBJ@HFCPNVEJ@YJHSEXBEQEQ#RVKXYVFSY#U#OQRMVWDQBWQUQPY#LNR@FXEOJWJALFJGT@SL#TABIE#FNREJKVXPIV#RTXNOHJLSZJBDKVHIBTAIUQNUIPA@ORQRZLDUBTHZOXSMJQYXCZPIEOJWJALSXHDHMGCJQZF#ME#BIFECUSYOTQXAVUZDTAG@HTBTCUKOQGDLFZC@SMNEQSHFJMKL@#XGWJUXSURVKX@CEGMAUILWOSGAWOWCENO@FHJKPYR@EMZDVZ@#NOVB@HIBY#UY#PFNA@#SY")
    chars = GetSymbolCount(ciphertext)
    missing_digrams = GetMissingPairs(ciphertext)
    monogram_list = RemoveDuplicates(list(ciphertext))

    missing_no_doubles = list(filter(lambda x: x[0] != x[1], missing_digrams))
    missing_swapped = ["" + x[1] + x[0] for x in missing_no_doubles]
    missing_swapped.sort()

    keyword_digrams = []

    for i in range(10):
        rows, cols = GetRowsColumns(missing_swapped, monogram_list)
        iteration_keyword_digrams = GetKeywordDigrams(rows, cols, chars)
        keyword_digrams += iteration_keyword_digrams
        firsts_banned, lasts_banned = GetBannedLetters(iteration_keyword_digrams)


        def IsValid(digram):
            return not ((digram[0] in firsts_banned) or (digram[1] in lasts_banned))


        missing_swapped = list(filter(IsValid, missing_swapped))

        if not iteration_keyword_digrams:
            print("No new info.. breaking")
            break

        print("\n\n")
        print(f"Keyword Digrams: {iteration_keyword_digrams}")
        print(f"Total Keyword: {keyword_digrams}")
        print(f"New Missing Digrams: {missing_swapped}")
        input("Next Interation...")

    keyword_digrams = list(set(keyword_digrams))

    print("\n\n")
    keyword_digrams.sort()
    print(", ".join(keyword_digrams))

    keyword = WhitespaceFormat(input("\n\nKeyword: "))

    best_fitness = 10
    best_plaintext = ""

    for i in range(len(keyword)):
        rotated = RotateList(keyword, i)
        plaintext = DecryptWithKeyword(ciphertext, rotated)
        fitness = abs(IndexOfCoincidence(plaintext) - ENGLISH_IOC)
        print(f"{i} | Plaintext: {plaintext[:20]} | Keyword: {rotated} | Fitness: {fitness}")

        if fitness < best_fitness:
            best_fitness = fitness
            best_plaintext = plaintext

    print("\n\n\n")
    print(best_plaintext)


    
    
    
    
    
        
        
        
        
        