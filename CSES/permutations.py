


n = int(input())
c = 1

if (n == 3 or n == 2):
    print("NO SOLUTION")
if (n == 4):
    print("2 4 1 3 ")
else:
    if (n % 2 == 0):
        print(n,end=' ')
        n -= 1
    for i in range(n):
        print((c % n)+1,end=' ')
        c += 2
print("")