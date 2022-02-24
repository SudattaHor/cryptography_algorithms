# finding g^a mod m
# (think of the algorithm as truncating the binary representation of a
def pow_mod(g, a, m):
    b = 1
    while a != 0:
        if a % 2 == 1:
            b = (b * g) % m
        a, g = a // 2, g**2 % m
    return b
