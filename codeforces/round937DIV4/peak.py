


t = int(input())

while (t):
    a,b ,c = [int(x) for x in input().split()]
    if (a < b < c):
        print("STAIR")
    elif (a < b > c):
        print("PEAK")
    else:
        print("NONE")
    t -= 1