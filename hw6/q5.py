# Extended Euclidean Algorithm
# takes a and b integers
# returns x and y such that xa + yb = gcd(a, b)
def ext_gcd(a, b):
    x, y, z, w = 1, 0, 0, 1
    while b != 0:
        x, y, z, w = z, w, x - (a // b) * z, y - (a // b) * w
        a, b = b, a % b
    return x, y


# finding g^a mod m
# (think of the algorithm as truncating the binary representation of a
def pow_mod(g, a, m):
    b = 1
    while a != 0:
        if a % 2 == 1:
            b = (b * g) % m
        a, g = a // 2, g**2 % m
    return b


# Euclidean algorithm to compute GCD
def euclid_alg(a, b):
    while b != 0:
        a, b = b, a % b
    return a


p, g, A = 348149, 113459, 185149
D, S1, S2 = 153405, 208913, 209176
Dprime, S1prime, S2prime = 127561, 208913, 217800

g1 = euclid_alg(S2, p-1)
u, _ = ext_gcd(S2/g1, (p-1)/g1)

a = 72729
