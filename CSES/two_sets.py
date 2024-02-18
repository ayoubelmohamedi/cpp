

#arthimetic progression a_n = a_1 (n - 1)d
# n(a_1+a_n)/2 -> a_n is the last term rather than the sum, 
# at 7th we have 7 for natural numbers 1,2,3..
 

n = int(input())
s = n*(1+n)// 2
print("s=",s)
seq = []
seq2 = []
curr = 0
if (s % 2 == 0):
    s = s//2
    l = 1
    r = n
    while (curr != s):
        if (l + r < s):
            curr = l + r
            
            seq.append(i)
        else:
            seq2.append(i)
    print(j)
    print(seq)
    print(n - j)
    print(seq2)
else:
    print("NO")