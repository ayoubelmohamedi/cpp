

#arthimetic progression a_n = a_1 (n - 1)d
# n(a_1+a_n)/2 -> a_n is the last term rather than the sum, 
# at 7th we have 7 for natural numbers 1,2,3..
 
def getterm(nbr : int) -> int:
    return (nbr*(1+nbr)//2)

n = int(input())
t = getterm(n)
half_t = t / 2
half = n // 2
seq2 = []
if (t % 2 == 0):
    print("yes")
    if (half_t == n):
        for i in range(1,n):
            print(i, end=" ")
        print("")
        print(n)
    
    pivot = getterm(half)
    curr = 0
    while (curr != half_t):
        print("pivot + n = {}, half_t => {}".format(pivot + n, half_t))
        if (pivot + n > half_t):
            diff = (pivot + n) - half
            seq2.append(diff)
            half += 1
            pivot = getterm(half)
            curr = (pivot + n) - diff
        else:
            print("here")
            half += 1
            pivot = getterm(half)
    print("seq2 => ",seq2)
#     print("YES")
#     diff = 0
#     head = n // 2
#     print("head => ", head)
#     print("get_term(head) = ",getterm(head))
#     half_t = int(half_t)
#     print("hald_t => ", half_t)
#     curr = 0
#     seq2 = []
#     print("n => ", n)
#     while (curr != half_t):
#         print("half_t => ", half_t)
#         tocmp = n + getterm(head)
#         print("tocmp => ",tocmp)
#         if (tocmp <= half_t):
#             curr = n + getterm(head)
#             head += 1
#             print("head is now ", head)
#             print("curr is now => ", curr)
#         else:
#             diff =  half_t - (n + getterm(head))
#             print("diff => ",diff)
#             seq2.append(abs(diff))
#             curr -= diff
#             break
#     print("----------------------")
#     print("head is ",head)
#     seq = list(range(1, head))
#     seq.pop(abs(diff )- 1)
#     seq.append(head)
#     seq.append(n)

# if (n )
#     print("seq => ",seq)
#     print("seq22  =>",seq2)
