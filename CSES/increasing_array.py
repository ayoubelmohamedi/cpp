


n = int(input())
nbrs = str(input())
nbrs = nbrs.split()
ls = [int(item) for item in nbrs]

res = 0

for i in range(1, len(ls)):
    if (ls[i - 1] > ls[i]):
        res += ls[i - 1] - ls[i]
        ls[i] = ls[i -1]
print(res)