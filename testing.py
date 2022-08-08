def biscuit(num):
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

