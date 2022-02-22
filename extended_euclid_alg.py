# Extended Euclidean Algorithm

def ext_gcd(a, b):
    x, y, z, w = 1, 0, 0, 1
    while b != 0:
        x, y, z, w = z, w, x - (a // b) * z, y - (a // b) * w
        a, b = b, a % b
    return x, y
