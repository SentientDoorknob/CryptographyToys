import random

from Imports.CipherEncoders import *

LEN = 250

encoders = [CaesarEncoder(LEN), VignereEncoder(LEN), SubstitutionEncoder(LEN//2), AffineEncoder(LEN), 
            PermutationEncoder(LEN), NihilistEncoder(LEN), HillEncoder(LEN), ColumnarEncoder(LEN),
            CadenusEncoder(LEN)]
encoder_includes = [True for i in range(len(encoders))]


def GetRandom():
    active_encoders = []
    for i in range(len(encoders)):
        if encoder_includes[i]:
            active_encoders.append(encoders[i])
    return random.choice(active_encoders)
