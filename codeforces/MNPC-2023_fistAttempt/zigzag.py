

n = int(input())
ls = str(input()).split()

def valid(end, i,arr):
    tmp = i
    res = 0
    for index in range(1,end,2):
        print("ODD checking index {} with {}".format(index,arr[index]))
        if arr[i] < arr[index]:
            i = index
    if i == end:
        printf("found ")
        res += 1
    for index in range(2,end,2):
        print("EVEN checking index {} with {}".format(index,arr[index]))
        if arr[tmp] > arr[index]:
            tmp = index
    if (tmp == end):
        res += 1
    return res

ls = [int(item) for item in ls]
res = 0
for i in range(len(ls) - 1):
    res += valid(n -1, i, ls)
    print("---------")
print(res)