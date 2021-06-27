def solution(x):
    y=sum(map(int,list(str(x))))
    if x%y==0:
        answer=True
    else:
        answer=False
    return answer