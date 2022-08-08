#There is a shop that offers a free Biscuit if you buy 2 Biscuits form there 
#Define a Function that calculates the price if a certain amount of Biscuits Example : If you want to take 11 Biscuits then the price should be 40
#Take the number of Biscuits as input from the user 


def biscuit():
    num = int(input('>'))
    free = 0
    initial = 0
    if num % 2 ==0:
        for i in range(num):
            initial = initial +2
            if initial < num:
                free = free+1
                initial = initial +1
    else:
        for i in range(num - 1):
            initial = initial + 2
            if initial < num:
                free = free + 1
                initial = initial + 1

    cost = (num - free) * 5
    return cost

