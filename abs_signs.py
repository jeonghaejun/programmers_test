def solution(absolutes, signs):
    sum_list = []
    for x, y in zip(absolutes, signs):
        if y == True:
            y = 1
        else:
            y = -1
        z = x*y
        sum_list.append(z)
    answer = sum(sum_list)
    return answer

# 다른사람 풀이


def solution(absolutes, signs):
    answer = 0
    for a, b in zip(absolutes, signs):
        if b:
            answer += a
        else:
            answer -= a
    return answer


def solution(absolutes, signs):
    return sum(a if b else -a for a, b in zip(absolutes, signs))


absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))
