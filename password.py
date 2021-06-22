import string


def solution(s, n):
    s = list(s)
    list_lower = string.ascii_lowercase
    list_upper = string.ascii_uppercase
    for index, word in enumerate(s):
        if word==' ':
            continue
        elif word.islower():
            s[index] = list_lower[(list_lower.find(word)+n)%26]
        else:
            s[index] = list_upper[(list_upper.find(word)+n)%26]
    return ''.join(s)


s = 'a B z'
n = 4
print(solution(s, n))

