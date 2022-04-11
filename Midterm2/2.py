"""
Decryption of RSA when modulus is too small
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

# Fast powering alg
def pow_mod(g, a, m):
    b = 1
    while a != 0:
        if a % 2 == 1:
            b = (b * g) % m
        a, g = a // 2, g**2 % m
    return b

class IdObj:
    pass
identity = IdObj()

class EllipticCurve:
    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p

    def invert(self, a):
        gg = gcd(a, self.p)
        if gg == 1:
            return ext_gcd(a, self.p)[0]
        else:
            print(f"{self.p} is not prime! {gg} is a factor!")
            return None

    def add(self, P1, P2):
        if P1 == identity:
            return P2
        if P2 == identity:
            return P1
        x1, y1 = P1
        x2, y2 = P2
        if x1 == x2 and (y1 + y2) % self.p == 0:
            return identity
        if P1 == P2:
            inv = self.invert(2 * y1)
            if inv is None:
                return None
            lam = ((3 * x1 ** 2 + self.A) * inv) % self.p
        else:
            inv = self.invert(x2 - x1)
            if inv is None:
                return None
            lam = ((y2 - y1) * inv) % self.p
        x3 = (lam ** 2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return x3, y3

    def mult(self, P, n):
        Q = P
        R = identity
        while n > 0:
            if n % 2 == 1:
                R = self.add(R, Q)
                if R is None:
                    return None
            Q = self.add(Q, Q)
            if Q is None:
                return None
            n = n // 2
        return R

# returns true on success
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

N = 14346535107930905316063751025780637288791306600123
e = 65537
c = 407648984592091521316401420379084752384663849948

while not lenstra_factor(N, 5000):
    pass

# Decrypt m with known p and q
p = 155673768585523
q = 92157691294338410542801545534170201
d = ext_gcd(e, (p-1)*(q-1))[0]
m = pow_mod(c, d, N)
print(f"d: {d}\nm: {m}")