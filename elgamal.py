from random import randrange


def ext_gcd(a, b):
    x, y, z, w = 1, 0, 0, 1
    while b != 0:
        x, y, z, w = z, w, x - (a // b) * z, y - (a // b) * w
        a, b = b, a % b
    return x, y


def pow_mod(g, a, m):
    p = 1
    while a != 0:
        if a % 2 == 1:
            p = (p * g) % m
        a = a // 2
        g = g ** 2 % m
    return p


p = 9853457983475897869054869759765789357890385093475093475803478054768221
g = 3458973489576784567897568954790348590839045745760547680547049750935709


def e(A, m):
    k = randrange(p)
    return pow_mod(g, k, p), (m * pow_mod(A, k, p)) % p


def d(a, c):
    return (c[1] * ext_gcd(pow_mod(c[0], a, p), p)[0]) % p
