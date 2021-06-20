def solution(nums):

    N = len(nums)/2
    ponketmon = list(set(nums))
    if len(ponketmon) >= N:
        answer = N
    else:
        answer = len(ponketmon)

    return answer

# 둘중의 작은숫자가 폰켓몬 선택 개수 획기적이군!!
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
