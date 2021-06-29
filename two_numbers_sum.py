from itertools import combinations


def solution(numbers):
    answer = []
    for i, j in list(combinations(numbers, 2)):
        if i+j not in answer:
            answer.append(i+j)
    answer.sort()

    return answer

# 희원님 짠거 굿~~
def solution(numbers):
    return sorted(list(set(map(sum,combinations(numbers,2)))))

numbers=[2,1,3,4,1]
print(solution(numbers))