
from math import log10
from math import floor


a = [10,11,12,13,14,15]

i = 10
pos = 17 
c = ''
print

dg = floor(log10(pos)) + 1
loc = floor((pos - i) // dg)
i += (pos - i) - 1

nbr = a[loc]
for c in str(nbr):
    if (i == pos):
        print(c)
    i += 1

print(nbr)
# jmp = i + loc *  dg

print(c)