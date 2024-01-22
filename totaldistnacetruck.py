
def distanceTraveled(mainTank: int, additioanlTank: int) -> int:
    c = 0
    while (mainTank > 0):
        c += 1
        mainTank -= 1
        if ((c % 5 == 0) and additioanlTank > 0):
            mainTank += 1
            additioanlTank -= 1
    return c  * 10

import math

def distanceTraveled2(mainTank: int, additionalTank: int) -> int:
    remain = additionalTank  - math.floor(mainTank // 5) 
    if (remain < 0):
        remain = additionalTank
    else:
        remain = math.floor(mainTank // 5) 
    return (mainTank + remain) * 10
    

if __name__ == '__main__':
    print(distanceTraveled2(4,12)) 