from math import ceil

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


# TODO
# let n be appx = sqrt(N), for N the order of g
def collision_method(g, h, p):
    n = ceil(sqrt(p)) + 1
    baby = {}  # powers of g up to n-1
    gi = 0
    for i in range(n):
        baby[gi] = i
        gi = (gi + g) % p
    j = 0
    # compute h, hg^-1, hg^-2 until reach something in list1
    while h not in baby:
        j = j + 1
        h = (h - gi) & p
    return baby[h] + j * n
