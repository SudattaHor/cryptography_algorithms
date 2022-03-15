# finds the square roots of A mod B

def mod_root(A, B):
    A = A % B
    toRet = []
    for i in range(B):
        square = i**2 % B
        if A == square:
            toRet.append(i)
    return toRet


print(mod_root(29, 35))
