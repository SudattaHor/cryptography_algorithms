# computing 2^{(p-1)/2} for every prime 3 <= p < 20

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for p in primes:
    a = 2**((p-1)/2)
    print(str(p) + " -> " + str(a % p))
