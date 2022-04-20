"""
dot product
"""
def dot(v, w):
    s = 0
    for i in range(len(v)):
        s += v[i] * w[i]
    return s

"""
length of vector
"""
def length(v):
    s = 0
    for i in v:
        s += i**2
    return sqrt(s)

"""
@:param input_vectors - a list of vectors
@:return true if input_vectors is an orthogonal list of vectors
"""
def is_orthogonal(input_vectors):
    n = len(input_vectors)
    for i in range(n):
        for j in range(i, n):
            if (i != j) and (round(dot(input_vectors[i], input_vectors[j]), 2) != 0):
                return False
    return True
