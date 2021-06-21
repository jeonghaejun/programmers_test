import re

def solution(new_id):
    new_id=new_id.lower()
    new_id=re.sub('[~!@#$%^&*()=+[{]}:?,<>/]','',new_id)
    for i in range(1,len(new_id)):
        if new_id[i-1]!=new_id[i]
    print(new_id)
    

    return new_id
    

new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id))