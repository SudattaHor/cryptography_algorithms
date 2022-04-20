"""
Solving the subset sum problem assuming that the sequence of integers form a
super increasing sequence
"""

import numpy as np

"""
@:param M, a list of superincreasing numbers
        S, the desired sum
@:return a list of 0s and 1s indicating which numbers in M sum to S
        if all 0s, either S = 0 or no solution
"""
def super_subset_solve(M, S):
    x = np.zeros(len(M))
    for i, m in enumerate(M[::-1]):
        if S >= m:
            x[len(M)-i-1] = 1
            S -= m
    return x

# M = np.array([4, 12, 15, 36, 75, 162])
# S = 214
# x = super_subset_solve(M, S)
# valid = (S == np.sum(M * x))
# print(f"x: {x}")
# print(f"valid: {valid}")