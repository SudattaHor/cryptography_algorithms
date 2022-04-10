"""
Class for an Elliptic Curve over real numbers

An elliptic curve is a set of points that satisfy the equation
y^2 = x^3 + A x + B
"""

import matplotlib.pyplot as plt
import numpy as np


class EllipticCurve:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    # finds the "sum" of two points
    def add(self, P1, P2):
        x1, y1 = P1
        x2, y2 = P2
        if P1 == P2:
            lam = (3 * x1 ** 2 + self.A) / (2 * y1)
        else:
            lam = (y2 - y1) / (x2 - x1)
        x3 = lam ** 2 - x1 - x2
        y3 = lam * (x1 - x3) - y1
        return x3, y3

    # "sums" point P to itself n times
    def mult(self, P, n):
        ret = P
        i = 1
        while i < n:
            ret = self.add(P, ret)
            i += 1
        return ret

    def plot(self, xmin, xmax, ymin, ymax):
        xx = np.linspace(xmin, xmax)
        yy = np.linspace(ymin, ymax)
        xx, yy = np.meshgrid(xx, yy)
        zz = yy**2 - xx**3 - self.A*xx - self.B
        plt.contour(xx, yy, zz, [0])
