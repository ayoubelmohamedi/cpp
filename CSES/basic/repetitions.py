

str = input()
res = 0
c = str[0]
curr = 0
for i,v in enumerate(str):
    if c == v:
        curr += 1
    else:
        res = max(res,curr)
        curr = 1
        c = v
res = max(res,curr)
print(res)