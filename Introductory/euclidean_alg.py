"""
Euclidean Algorithm
@:param a and b integers
@:return gcd(a, b) using the Euclidean Algorithm
"""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

"""
Extended Euclidean Algorithm
@:param a and b integers
@:return x and y such that xa + yb = gcd(a, b)
"""
def ext_gcd(a, b):
    x, y, z, w = 1, 0, 0, 1
    while b != 0:
        x, y, z, w = z, w, x - (a // b) * z, y - (a // b) * w
        a, b = b, a % b
    return x, y
