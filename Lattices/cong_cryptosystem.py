"""
A congruential cryptosystem
"""
import math
import random

from Introductory.euclidean_alg import *

class CongCryptosystem:

    """
    Sets up public key given private integers f and g and given public modulus q
    @:param q, a large public modulus
            f, a secret integer such that f < sqrt(q/2)
            g, a secret integer such that such that sqrt(q/4) < g < sqrt(q/2)
    @:return nothing
    """
    def __init__(self, q, f, g):
        assert f < math.sqrt(q / 2)
        assert math.sqrt(q / 4) < g < math.sqrt(q / 2)
        assert gcd(f, q * g) == 1
        finv = ext_gcd(f, q)[0]
        h = (finv * g) % q
        self.public_key = (q, h)

    """
    Encrypts a message
    @:param m, message to be encrypted
    @:return e, the encrypted message
    """
    def encrypt(self, m, r=None):
        q, h = self.public_key
        if r is None:
            r = random.randint(1, math.floor(math.sqrt(q) / 2))
        assert 0 < m < math.sqrt(q)
        e = (r * h + m) % q
        return e

    """
    Decrypts a message
    @:param e, message to be decrypted
            priv_key, the private key (f, g)
    @:return m, the decrypted message
    """
    def decrypt(self, e, priv_key):
        q, h = self.public_key
        f, g = priv_key
        finv = ext_gcd(f, g)[0]
        a = (f * e) % q
        print(f"a: {a}")
        m = (finv * a) % g
        return m

f, g = 19928, 18643
q = 918293817
e = 619168806
r = 19564
m = 10220

Crypt = CongCryptosystem(q, f, g)
print(f"public key: {Crypt.public_key}")
print(f"m: {Crypt.decrypt(e, (f, g))}")
print(f"e: {Crypt.encrypt(m, r)}")
