def solution(phone_number):
    x=len(phone_number)-4
    y='*'*x
    print(y)
    answer=phone_number.replace(phone_number[0:x],y)
    return answer

def solution(s):
    return "*"*(len(s)-4) + s[-4:]
