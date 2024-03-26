



n = 7
goal = int((n*(n+1)) / 2)

res = 0
remain = 0
if (goal % 2 == 0):
    while (remain != n):
        if (remain > n):
            remain = remain + abs(n)
        else:
            remain = remain + n

            remain = remain + n
        n = n - 1