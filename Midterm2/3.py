"""
Forging DSA signature given that modulus is too small
"""

import math
import random

# Extended Euclidean Algorithm
def ext_gcd(a, b):
    x, y, z, w = 1, 0, 0, 1
    while b != 0:
        x, y, z, w = z, w, x - (a // b) * z, y - (a // b) * w
        a, b = b, a % b
    return x, y

# Euclidean algorithm to compute GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fast powering algorithm
def pow_mod(g, a, m):
    b = 1
    while a != 0:
        if a % 2 == 1:
            b = (b * g) % m
        a, g = a // 2, g**2 % m
    return b

def baby_giant_mult(g, h, p):
    n = math.ceil(math.sqrt(p)) + 1
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

def sign(g, p, q, a, d):
    k = random.randrange(2, q)
    kinv, _ = ext_gcd(k, q)
    s1 = pow_mod(g, k, p) % q
    s2 = (d + a*s1)*kinv % q
    return s1, s2

def verify(S, D, p, q, V, g):
    s1, s2 = S
    s2inv, _ = ext_gcd(s2, q)
    v1 = D*s2inv % q
    v2 = s1*s2inv % q
    return s1 == pow_mod(g, v1, p) * pow_mod(V, v2, p) % p % q


p = 2040601214665943
q = 1020300607332971
g = 247235222966191
V = 27842090425483
D = 87391730419568
a = baby_giant_mult(g, V, p)
S = sign(g, p, q, a, D)
print(f"a: {a}")
print(f"S: {S}")
print(f"Valid signature: {verify(S, D, p, q, V, g)}")
