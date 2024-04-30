


def power_efficient(a, b,m) -> int:
    a %= m
    res  = 1
    while (b > 0):
        if (b&1):
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return (int(res))

m = 10e9 + 7
t = int(input())
while (t > 0):
    val = input().split()
    a, b = int(val[0]), int(val[1])
    print(power_efficient(a,b, m))
    t -= 1