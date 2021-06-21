import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub(
        '[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]', '', new_id)
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    if new_id[0] == '.':
        new_id=new_id.replace('.','',1)

    if new_id[len(new_id)-1] == '.':
        new_id=list(new_id)
        new_id[len(new_id)-1] = ''
        new_id=''.join(new_id)
    # 5단계
    new_id=new_id.strip()
    print('start'+new_id+'end')

    # 6단계
    if len(new_id)>=16:
        new_id=new_id[0:14]
    
    print('start'+new_id+'end')

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm."

print(solution(new_id))
