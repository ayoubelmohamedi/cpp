
t = int(input())
i = 0
res = []
def getanchor(cor : set) -> int:
    n = max(cor)
    return (n**2) - (n - 1)

while (i < t):
    y,x  = map(int,input().split())
    mx = max(y,x)
    anchor = getanchor((y,x))
    if (x == y):
        res.append(anchor) 
        i += 1
        continue
    # vertical is decrease, horizental is increase for anchor % 2
    diff = mx - min(y,x)
    if (mx % 2 == 0):
        #vertical
        if (y < mx):
            res.append(anchor - diff)
        #horizental
        else:
            res.append(anchor + diff)
    else:
        #(horizental) y < mx
        if (y < mx):
            res.append(anchor + diff)
        else:
            res.append(anchor - diff)
    i += 1
for j in res:
    print(j)