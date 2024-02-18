

n = int(input())
ls = [int(i) for i in input().split()]

res = (n*(1+n))//2
print(res - sum(ls))