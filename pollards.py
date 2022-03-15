from fast_powering import *
import numpy as np


def factor(N, a=2):
    i = 1
    while np.gcd(a-1, N) == 1:
        i += 1
        a = pow_mod(a, i, N)
    return np.gcd(a-1, N)
