"""
Algorithm for the Gram Schmidt algorithm
"""

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
Gram-Schmidt alg
@:param input_vectors - a list of vectors that form a basis for V
@:return output - a list of vectors that form an orthogonal basis for V
"""
def gram_schmidt(input_vectors):
    M = []
    for v in input_vectors:
        for w in M:
            mu = dot(w, v) / dot(w, w)
            for i in range(len(v)):
                v[i] = round(v[i] - mu * w[i], 3)
        M.append(v)
    return M

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

vv = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7]]
print(f"output: {gram_schmidt(vv)}")
print(f"valid: {is_orthogonal(gram_schmidt(vv))}")