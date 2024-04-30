



t = int(input())


while (t):
    n , a , b = [int(x) for x in input().split()]    
    if (2*a < b):
        print(a * n)
        t -= 1
        continue
    if (n&1):
        print("is odd")
        print(n/2 * b + a)
    else:
        print("is even")
        print(n/2 * b)
    t -= 1