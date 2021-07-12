def solution(a, b):
    if a>b:
        a,b=b,a
    sum_list=list(range(a,b+1))
    
    return sum(sum_list)