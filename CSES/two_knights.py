

def get_combo(nbr : int) -> int:
    places = ((nbr*nbr) * ((nbr*nbr) - 1))// 2 
    attacks = 4*(nbr-1)*(nbr-2)
    return (places - attacks)

n = int(input())

if (n > 0):
    for i in range(1,n+1):
        print(get_combo(i))
