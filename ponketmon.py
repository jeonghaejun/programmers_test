def solution(nums):
    
    N=len(nums)/2
    ponketmon=list(set(nums))
    if len(ponketmon)>=N:
        answer=N
    else:
        answer=len(ponketmon)
    
    return answer