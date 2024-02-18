

#arthimetic progression a_n = a_1 (n - 1)d
# n(a_1+a_n)/2 -> a_n is the last term rather than the sum, 
# at 7th we have 7 for natural numbers 1,2,3..
 

n = int(input())
s = n*(1+n) / 2
l, r = 1, n
tot = 0 
arr = [item for item in range(1,n+1)]
seq1 = []
seq2 = []
goal = int(s) // 2

if (s % 2 == 0):
    print("YES")
    while (l < r):
        if (l % 2 != 0):
            seq1.append(l)
            seq1.append(r)
            tot = l + r
        else:
            seq2.append(l)
            seq2.append(r)
        l += 1
        r -= 1

    if (n % 2 != 0 and s % 2 == 0):
        diff = goal - tot
        if (diff != 0):
            #need to fix this.>
            seq2.append(seq1[-1])
            seq2.append(seq1[-2])
            #nbr in the middle is 'l'
            seq2.append(l)

            seq1.remove(seq1[-1])
            seq1.remove(seq1[-1])

            seq2.remove(diff)
            seq1.append(diff)

    print(len(seq1))
    print(sorted(seq1))
    print(len(seq2))
    print(sorted(seq2))
else:
    print("NO")
