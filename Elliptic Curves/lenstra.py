import numpy as np
from elliptic_curve_f import *


def lenstra_factor(N):
    A = np.random.randint(N)
    a = np.random.randint(N)
    b = np.random.randint(N)
    P = (a, b)
    B = (b**2 - a**3 - A*a) % N
    E = EllipticCurve(A, B, N)
    for j in range(int(np.sqrt(N))):
        Q = E.mult(P, j)
        if Q is None:
            return
    print("Factoring unsuccesful")
