import math


def solution(left, right):
    list1 = []
    list2 = []
    for i in range(left, right+1):
        if int(math.sqrt(i)) == math.sqrt(i):
            list1.append(i)
        else:
            list2.append(i)

    return sum(list2)-sum(list1)


left = 13
right = 17

print(solution(left, right))
