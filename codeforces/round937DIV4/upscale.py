



t = int(input())
a = "##"
b = ".."
l = [a,b]
while (t):
    n = int(input())
    shape = ""
    shape2 = ""

    for i in range(n):
        shape += l[i%2]
        shape2 += l[(i+1)%2] 
    s = [shape,shape2]
    for i in range(n): 
        print(s[i%2])
        print(s[i%2])
    t -= 1