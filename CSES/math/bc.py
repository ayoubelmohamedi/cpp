
from math import factorial as fac

def comb(a, b):
    return (fac(a) / (fac(b) * fac(a - b)))

t = int(input())
while (t > 0):
    n = input().split()
    a, b = int(n[0]), int(n[1])
    print(int(comb(a, b)) % (10**9 + 7))
    t -= 1