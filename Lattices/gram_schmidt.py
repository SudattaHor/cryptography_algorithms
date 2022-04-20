"""
Algorithm for the Gram Schmidt algorithm
"""

from linalg import *

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

vv = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7]]
print(f"output: {gram_schmidt(vv)}")
print(f"valid: {is_orthogonal(gram_schmidt(vv))}")