import numpy as np
from elliptic_curve_f import *


def lenstra_factor(N):
    P = Pp = (2, 5)
    E = EllipticCurve(4, 9, N)
    j = 0
    while j < np.sqrt(N):
        Pp = E.add(Pp, P)
        if Pp is None:
            return
        j += 1
    lenstra_factor(N)


lenstra_factor(589)
