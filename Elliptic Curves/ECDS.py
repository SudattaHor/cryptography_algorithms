"""
Class for Elliptic Curve Digital Signature Algorithm
"""


class ECDSA:
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
        s2 = ((self.d + s * s1) * einv) % self.q
        return s1, s2

    def verify(self, s1, s2, V):
        s2inv = ext_gcd(s2, self.q)[0]
        v1 = (self.d * s2inv) % self.q
        v2 = (s1 * s2inv) % self.q
        print(v1, v2)
        candidate = self.E.add(self.E.mult(self.G, v1), self.E.mult(V, v2))
        return candidate[0] % self.q == s1
