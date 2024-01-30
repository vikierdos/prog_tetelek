import math


def prim_eldontes():
    prim = False
    n = 9999
    while not prim:
        n += 1
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    print(n)

prim_eldontes()