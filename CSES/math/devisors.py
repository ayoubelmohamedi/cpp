

from math import floor

def divs(n : int) ->int :
    res = 0
    i = 1
    m = floor(n / 2)
    if (n > 1 and n % 2 != 0):
        return (2)
    if (n % 2 != 0):
        return (1)
    while (i < m):
        if (m % i):
            res += 1
        i += 1
    return (res)

t = int(input())
while (t > 0):
    val = int(input())
    print(divs(val))
    t -= 1