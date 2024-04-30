n = int(input())
p = [int(x) for x in  input().split()]

p = sorted(p)

s = sum(p)
remain = s // 2

l , r = 0, len(p) - 1
tmp = 0
g1 = []
print("sum is => ",s)
print("remain is => ", remain)


print("r => ",r)
while (l < r):
    if (tmp >= remain):
        break 
    if (p[r] + tmp <= remain):
        tmp += p[r]
        r -= 1
    elif (p[l] + tmp <= remain):
        tmp += p[l]
        l += 1

    
print("tmp => ",tmp)

        
