from random import randrange
from Introductory.euclidean_alg import *
from Introductory.fast_powering import *

p = 9853457983475897869054869759765789357890385093475093475803478054768221
g = 3458973489576784567897568954790348590839045745760547680547049750935709


# encryption function:
# takes in Alice's message A (= g^a, unknown to encryptor)
# returns (c1, c2) = (g^k, mA^k)
def e(A, m):
    k = randrange(p)
    return pow_mod(g, k, p), (m * pow_mod(A, k, p)) % p


# decryption function:
# takes in (c1, c2)
# returns message m = (c1^a)^(-1) * c2
def d(a, c):
    return (c[1] * ext_gcd(pow_mod(c[0], a, p), p)[0]) % p
