import math
import random
from elliptic_curve_f import *

def lenstra_factor(N, k):
    A = random.randrange(N)
    a = random.randrange(N)
    b = random.randrange(N)
    print(f"A: {A}\na: {a}\nb: {b}\n")
    P = (a, b)
    B = (b**2 - a**3 - A*a) % N
    E = EllipticCurve(A, B, N)
    for j in range(2, k):
        Q = E.mult(P, j)
        if Q is None:
            return True
        P = Q
    print("Factoring unsuccesful")
    return False
