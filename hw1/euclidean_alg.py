# Euclidean algorithm to compute GCD
def euclid_alg(a, b):
    while b != 0:
        a, b = b, a % b
    return a
