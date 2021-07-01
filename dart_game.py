import re


def solution(dartResult):
    answer = []
    pattern = r'\d+\w\#|\d+\w\*|\d+\w'
    s = re.compile(pattern)
    list1 = s.findall(dartResult)
    print(list1)
    for index, x in enumerate(list1):
        if '#' in x:
            if 'S' in x:
                answer.append(int(x[:-2])*(-1))
            elif 'D' in x:
                answer.append(int(x[:-2])**2*(-1))
            elif 'T' in x:
                answer.append(int(x[:-2])**3*(-1))

        elif '*' in x:
            if 'S' in x:
                answer.append(int(x[:-2])*2)
            elif 'D' in x:
                answer.append(int(x[:-2])**2*2)
            elif 'T' in x:
                answer.append(int(x[:-2])**3*2)
            if index>0:
                answer[index-1]=answer[index-1]*2

        elif 'S' in x:
            answer.append(int(x[:-1]))
        elif 'D' in x:
            answer.append(int(x[:-1])**2)
        elif 'T' in x:
            answer.append(int(x[:-1])**3)

    print(answer)

    return sum(answer)


dartResult = "1S*2T*3S"

# st='1S'
# print(st[:-1])
print(solution(dartResult))

# 희원님 풀이
import re

def solution(dartResult):
    dart=re.findall('\d+\D+',dartResult)
    answer = []
    for i in dart:
        num=int(re.search('\d+',i).group())
        if 'S' in i:
            j=num
        elif 'D' in i:
            j=num**2
        else:
            j=num**3
        if '#' in i:
            j=-j
        answer.append(j)

        if '*' in i:
            answer[-1]*=2
            try:
                answer[-2]*=2
            except: pass   
    
    return sum(answer)

# 다른사람 풀이

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

# 다른사람 풀이

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer