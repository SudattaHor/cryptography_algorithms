import matplotlib.pyplot as plt
import numpy as np
from extended_euclid_alg import *


# Elliptic Curve over finite field F_p
class EllipticCurve:
    def __init__(self, A, B, p):
        self.A = A
        self.B = B
        self.p = p
        self.O = "identity"
        self.solutions = self.find_points()

    def find_points(self):
        # FIND QUADRATIC RESIDUES MOD P
        quad_residues = {}
        for x in range(self.p):
            if (x ** 2 % self.p) not in quad_residues.keys():
                quad_residues[x ** 2 % self.p] = []
            quad_residues[x ** 2 % self.p].append(x)
        print(f"quadresidues: {quad_residues}")
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
        print(f"solutions: {ret}")
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
            inv, _ = ext_gcd(2 * y1, self.p)
            lam = ((3 * x1 ** 2 + self.A) * inv) % self.p
        else:
            inv, _ = ext_gcd(x2 - x1, self.p)
            lam = ((y2 - y1) * inv) % self.p
        x3 = (lam ** 2 - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return x3, y3

    def print_table(self):
        for P1 in self.solutions:
            row = [self.add(P1, P2) for P2 in self.solutions]
            print(row)


E = EllipticCurve(2, 3, 7)
E.print_table()
