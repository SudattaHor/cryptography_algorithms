"""
Factorization based off of Miler-Rabin test
"""
import math

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

def mrfactor(N, a):
    # write N-1 in the form of 2^k q
    q, k = N-1, 0
    while q % 2 == 0:
        k += 1
        q = q // 2
    # compute list
    c = pow_mod(a, q, N)
    if c == 1 or c == -1:
        print(f"{a} is not a Miller-Rabin Witness, try again.")
        return
    for i in range(k):
        candidate = pow_mod(c, 2, N)
        if candidate == 1:
            break
        if candidate == -1:
            print(f"{a} is not a Miller-Rabin Witness, try again.")
            return
        c = candidate
    return gcd(c+1, N), gcd(c-1, N)

# Use of mrfactor and Riemann hypothesis to check primality
def is_prime(N):
    a = 2
    while a < 2*math.log(N)**2:
        result = mrfactor(N, a)
        if result is None:
            a += 1
            continue
        x, y = result
        if (x != N) and (x != 1):
            print(f"{N} is composite with factors {x} and {N // x}")
            return False
        if (y != N) and (y != 1):

            print(f"{N} is composite with factors {y} and {N // y}")
            return False
        a += 1
    return True

N = 12158241101501440230790584910546542499394209724500115861996726125256174580421552000692841163237819606174149875504179377400373782507636714217242092622601198547164256682626321392956657652489104462967884772621590146469750489942306366762433333048623556301087055749926181178337670225742391340252398570943921
a, b = mrfactor(N, 2)
_, c = mrfactor(a, 2)
d = a // c
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

