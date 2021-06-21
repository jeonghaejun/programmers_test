
# 여벌의 체육복이 있는 친구도 도난당할수 있다.(함정)
def solution(n, lost, reserve):
    set_lost = set(lost)-set(reserve)  # 여분의 체육복이 있엇는데 도둑맞았을때
    set_reserve = set(reserve)-set(lost)  # 여분의 체육복이 있었는데 도둑맞아서 빌려줄수 없어욤

    for i in set_reserve:

        if i-1 in set_lost:  # i보다 작은값먼저 확인해야해!!!(중요!!)
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    return n-len(set_lost)


n = 5
lost = [2, 4]
reserve = [3]

print(solution(n, lost, reserve))
