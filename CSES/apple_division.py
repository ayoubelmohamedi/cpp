
#recurive
def weirdo(n:int):
    if (n == 1):
        print(1)
        return
    print(n,end=' ')
    if (n % 2 == 0):
        weirdo(n // 2)
    else:
        weirdo(n * 3 + 1)

n = int(input())
weirdo(n)