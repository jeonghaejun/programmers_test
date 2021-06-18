
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]  # 맞은 개수에 따른 순위 랭크 배열

    cnt_0 = lottos.count(0) # 모르는 번호 카운트
    ans = 0 # 번호 맞을때 맞다 1씩 증가

    for x in win_nums:  # for 문을 이용하여 로또 당첨번호와 대조 
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]