import math


def solution(n):
    list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            list.append(i)
            if i != n//i:
                list.append(n//i)
    return sum(list)
