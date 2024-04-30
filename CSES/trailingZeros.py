




from math import factorial

n = int(input())
f = str(factorial(n))

# def recur(nbr) -> int:
#     c = 0
#     while (nbr != 0):
#         tmp = 0
#         while (nbr % 10 == 0):
#             tmp += 1
#             nbr //=10
#         if (tmp > c):
#             c = tmp
#         nbr //=10
#     return c 

i = 0
c = 0

while (i < len(f)):
    tmp = 0
    while (f[i] == '0'):
        tmp += 1
        i += 1
    if (tmp > c):
        c = tmp
    i += 1
print(c)