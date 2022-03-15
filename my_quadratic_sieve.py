from extended_euclid_alg import *
from fast_powering import *
import numpy as np

# PARAMETERS
N = 493
B = 11
prime_powers = [2, 3, 5, 7, 11]  # p^e < B, where B = 11
a = 23
b = 38


def f(t):
    return int(t ** 2 - N)


def find_square(N, p):
    t = 0
    while t < p:
        if pow_mod(t, 2, p) == (N % p):
            return t, p - t
        t += 1
    return None


t_list = np.linspace(a, b, b - a + 1)
f_list = {t: f(t) for t in t_list}

print(list(f_list.values()))
for p in prime_powers:
    n = 1
    while p**n <= B:
        print(f"Sieving {p}^{n}:")
        if find_square(N, p**n) is None:
            n += 1
            print("No Solutions")
            continue
        alpha, beta = find_square(N, p**n)
        for t in t_list:
            if t % p**n == alpha or t % p**n == beta:
                f_list[t] = f_list[t] // p
        print(list(f_list.values()))
        n += 1
