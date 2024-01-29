



def modifystr(s, index,c):
    return (s[:index - 1] + c + s[index:])

def findstr(substr, stro, found):
    if substr in stro:
        start_index = stro.find(substr) + 1
        end_index = start_index + len(substr) 
        found.add((start_index,end_index))
        return start_index
    return -1

s = str(input())
n = int(input())

i = 0
found = set()
while (i < n):
    a = str(input())
    sp = a.split()
    if (a[0] == '1'):
        print(findstr(sp[1], s, found))
    elif (a[0] == '0'):
        index = int(sp[1])
        s = modifystr(s,index,sp[2])
        toberemoved = ()
        for item in found:
            if item[0] <= index <= item[1]:
                toberemoved = item
        if len(toberemoved) != 0:
            found.remove(toberemoved)
    i += 1