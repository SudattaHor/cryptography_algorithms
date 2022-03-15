from math import ceil
from math import floor
from math import sqrt
from extended_euclid_alg import *
from fast_powering import *

"""
Let p be an odd prime
Given h mod p, we want to find x such that g^x = h mod p

Note: the group operation is addition, working over Z/pZ
"""


# go through every power of g and check
def brute_force(g, h, p):
    i, gi = 0, 0
    while gi != h:
        i = i + 1
        gi = (gi + g) % p
    return i


def baby_giant_add(g, h, p):
    n = ceil(sqrt(p)) + 1  # let n be appx = sqrt(N), for N the order of g
    baby = {}  # powers of g up to n-1
    gi = 0
    for i in range(n):
        baby[gi] = i
        gi = (gi + g) % p
    j = 0
    # compute h, hg^-1, hg^-2 until reach something in list1
    while h not in baby:
        j = j + 1
        h = (h - gi) % p
    return baby[h] + j * n


def baby_giant_mult(g, h, p):
    n = ceil(sqrt(p)) + 1
    baby_list = {}
    gi = 1
    for i in range(n):
        baby_list[gi] = i
        gi = (gi*g) % p
    g_inv, _ = ext_gcd(g, p)
    g_n_inv = pow_mod(g_inv, n, p)
    j = 0
    while h not in baby_list:
        j += 1
        h = (h * g_n_inv) % p
    return baby_list[h] + j * n


print(baby_giant_mult(113459, 185149, 348149))
