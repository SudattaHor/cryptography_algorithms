import numpy as np
from extended_euclid_alg import *
from mod_root import *
from fast_powering import *


# Elliptic Curve over finite field F_p
class EllipticCurve:
    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p
        self.O = "identity"
        self.solutions = self.find_points()

    def findy(self, x):
        """
        Finds y coordinate of a point given the x coordinate
        :param x: x coordinate of point
        :return: corresponding y coordinate
        """
        y2 = (pow_mod(x, 3, self.p) + self.A * x + self.B) % self.p
        return mod_root(y2, self.p)

    def find_points(self):
        # FIND QUADRATIC RESIDUES MOD P
        quad_residues = {}
        for x in range(self.p):
            if (x ** 2 % self.p) not in quad_residues.keys():
                quad_residues[x ** 2 % self.p] = []
            quad_residues[x ** 2 % self.p].append(x)
        # FIND SOLUTIONS
        solutions = set()
        for x in range(self.p):
            rhs = (x ** 3 + self.A * x + self.B) % self.p
            if rhs in quad_residues:
                for y in quad_residues[rhs]:
                    solutions.add((x, y))
        ret = list(solutions)
        ret.sort(key=lambda y: y[0])
        ret.insert(0, self.O)
        return ret

    def add(self, P1, P2):
        if P1 == self.O:
            return P2
        if P2 == self.O:
            return P1
        x1, y1 = P1
        x2, y2 = P2
        if (y1 + y2) % self.p == 0:
            return self.O
        if P1 == P2:
            if np.gcd(2*y1, self.p) != 1:
                print(f"{self.p} is not prime! {np.gcd(2*y1, self.p)} is a factor!")
                return None
            inv, _ = ext_gcd(2 * y1, self.p)
            lam = ((3 * x1 ** 2 + self.A) * inv) % self.p
        else:
            if np.gcd(x2-x1, self.p) != 1:
                print(f"{self.p} is not prime! {np.gcd(x2-x1, self.p)} is a factor!")
                return None
            inv, _ = ext_gcd(x2 - x1, self.p)
            lam = ((y2 - y1) * inv) % self.p
        x3 = (lam ** 2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return x3, y3

    def mult(self, P, n):
        ret = P
        i = 1
        while i < n:
            ret = self.add(P, ret)
            i += 1
        return ret

    def log(self, P, Q):
        r = int(np.sqrt(self.p))
        jlist = {}
        jj = np.random.choice(self.p, r, replace=False)
        for j in jj:
            jlist[self.mult(P, j)] = j
        kk = np.random.choice(self.p, r, replace=False)
        for k in kk:
            candidate = self.add(Q, self.mult(P, k))
            if candidate in jlist.keys():
                n_candidate = (jlist[candidate] - k) % self.p
                if E.mult(P, n_candidate) == Q:
                    return n_candidate
        return self.log(P, Q)

    def print_table(self):
        for P1 in self.solutions:
            row = [self.add(P1, P2) for P2 in self.solutions]
            print(row)


class ECDS:
    def __init__(self, EllpCurve, G, q, document):
        self.E = EllpCurve
        self.G = G
        self.q = q
        self.d = document

    def sign(self, s, e):
        V = self.E.mult(self.G, s)
        print(f"Verification key V for secret signing key {s} is V = {V}")
        einv = ext_gcd(e, self.q)[0]
        s1 = self.E.mult(self.G, e)[0] % self.q
        s2 = ((self.d + s*s1)*einv) % self.q
        return s1, s2

    def verify(self, s1, s2, V):
        s2inv = ext_gcd(s2, self.q)[0]
        v1 = (self.d*s2inv) % self.q
        v2 = (s1*s2inv) % self.q
        print(v1, v2)
        candidate = self.E.add(self.E.mult(self.G, v1), self.E.mult(V, v2))
        return candidate[0] % self.q == s1

#
# E = EllipticCurve(231, 473, 17389)
# q = 1321
# G = (11259, 11278)
# Umberto = ECDS(E, G, q, document=993)
# s1, s2 = 907, 296
# print(Umberto.verify(s1, s2, (11017, 14637)))
