

from collections import defaultdict

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

s = input()
l = len(s)
dic = defaultdict(int)

for c in s:
    dic[c] += 1

c = 0
pv = 0
pk = 0
for k, v in dic.items():
    if v % 2 != 0:
        if (c == 0):
            pk = c
            pv = v
            c += 1
        else:
            c += 1
            break
if (c == 2):
    print("NO")
else:
    tmp = 1
    l = (len(dic) - pv) // 2
    i = 0
    res = ""
    for k, v in dic.items():
        if k == pk:
            continue
        res += k* (v // 2)
    res += pv * pk 
    for k , v in dic.items():
        if (k == pk):
            continue
        res += k* (v // 2)
    print("pv is {} and pk is {}".format(pv, pk))
    # res += pv * pk
    print(res)
        
    
    

# s = 'a'*5
# i = 0
# n = list(set(s))
# while (i <  l // 2):
#     t = dic[n[i]]
#     for time in range(t // 2):
#         s[i] = n[i]
#         s[-time] = n[i]

# tot = i + get_key_by_value(dic, dic[i])
# while (i < tot):
#     s[i] = pivot
#     i += 1
# print(s)
# print(dic)