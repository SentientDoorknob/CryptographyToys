import random

from Encoders import *
from Encoders.Ciphers.AffineEncoder import AffineEncoder
from Encoders.Ciphers.CaesarEncoder import CaesarEncoder
from Encoders.Ciphers.HillEncoder import HillEncoder
from Encoders.Ciphers.SubstitutionEncoder import SubstitutionEncoder
from Encoders.Ciphers.NihilistEncoder import NihilistEncoder
from Encoders.Ciphers.PermutationEncoder import PermutationEncoder
from Encoders.Ciphers.VignereEncoder import VignereEncoder

LEN = 250

encoders = [CaesarEncoder(LEN), VignereEncoder(LEN), SubstitutionEncoder(LEN//2), AffineEncoder(LEN), PermutationEncoder(LEN), NihilistEncoder(LEN), HillEncoder(LEN)]
encoder_includes = [True for i in range(len(encoders))]


def GetRandom():
    active_encoders = []
    for i in range(len(encoders)):
        if encoder_includes[i]:
            active_encoders.append(encoders[i])
    return random.choice(active_encoders)
