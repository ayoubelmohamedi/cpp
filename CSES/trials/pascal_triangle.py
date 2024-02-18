


n = int(input())
curr = 4
before = 5
res = [1,5]

for i in range(1,n-1):
    curr = curr * 2
    res.append(curr + before)
    before = res[-1]
if (n == 1):
    print(res[0])
else:
    print(res)