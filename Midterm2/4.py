"""
Solving Elliptic Curve Elgalmal when random key k is reused
"""

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

A = 0
B = 7
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
E = EllipticCurve(A, B, p)
C2 = (9226528006366587445106537596682453005742996612854399557725599750609385197637,
      73926754547015775924459898765546441033009666943031583779909664387933500699081)
C2p = (78104975042778607657425723091144918682383131690364372741738925434199106305718,
       21010532786068216810976007430741487214533339013300775603696563779733532423905)
Mp = (99287373940323529221189360923087516993717407550435679661582837078272328816008,
      59913291701092255631169855775932219631109095189166670153952385453247886347082)
minusC2p = (C2p[0], -C2p[1] % p)
print(f"M: {E.add(C2, E.add(minusC2p, Mp))}")