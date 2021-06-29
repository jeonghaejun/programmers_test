def solution(s):
    answer = ''
    x=int(len(s)/2)
    if len(s)%2==0:
        answer=s[x-1]+s[x]
    else:
        answer=s[x]
        
    return answer

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]