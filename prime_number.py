import math
import itertools

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    numbers_3_list = itertools.combinations(nums,3)
    for i in numbers_3_list:
        num=sum(i)
        if is_prime_number(num):
            answer+=1

    return answer