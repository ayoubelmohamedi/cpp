


from math import factorial

def perm(s):
    res = []
    if (len(s) == 1):
        return [s]
    for i in range(len(s)):
        hd = s[i]
        r = s[0:i] + s[i+1:]
        p = perm(r)
        for j in range(len(p)):
            res.append(hd + p[j])
    return res
# n = factorial(len(a))
# print(len(a))
# for i in range(1,n):
a = "aabac"
res = perm(a)
print(len(res))
print(res)
# np = = factorial(len(b) / )
# print(perm(b))

