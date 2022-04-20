"""
merkle hellman subset sum cryptosystem
"""

from linalg import *
from subset_sum_super import *
from Introductory.euclidean_alg import *

def is_superincreasing(rr):
    for i, r in enumerate(rr):
        if i == len(rr)-1:
            continue
        if 2*r > rr[i+1]:
            return False
    return True

class MerkleHellman:

    """
    Sets up the public key
    @:param r - super increasing sequence
            A, B - integers  such that B > 2r_n and gcd(A, B) = 1
    """
    def __init__(self, r, A, B):
        n = len(r)
        assert(is_superincreasing(r))
        assert(B > r[n-1])
        assert(gcd(A, B) == 1)
        M = []
        for ri in r:
            new_element = (A * ri) % B
            M.append(new_element)
        self.public_key = M

    def encrypt(self, x):
        return dot(x, self.public_key)

    @staticmethod
    def decrypt(r, A, B, S):
        Ainv = ext_gcd(A, B)[0]
        Sp = (Ainv * S) % B
        return super_subset_solve(r, Sp)


def find_r(M, A, B):
    Ainv = ext_gcd(A, B)[0]
    return [(m*Ainv) % B for m in M]

M = [5186, 2779, 5955, 2307, 6599, 6771, 6296, 7306, 4115, 637]
A = 4392
B = 8387
r = find_r(M, A, B)
S = 25916
CryptoSystem = MerkleHellman(r, A, B)
message = CryptoSystem.decrypt(r, A, B, S)
valid = S == dot(message, M)
print(f"r: {r}")
print(f"message: {message}")
print(f"valid: {valid}")