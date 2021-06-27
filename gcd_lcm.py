def solution(n, m):
    answer = []
    a, b = n, m
    if m < n:
        x = n
        n = m
        m = x
    while n > 0:
        y = n
        n = m % n
        m = y
    answer.append(m)
    c = a/m
    d = b/m
    answer.append(int(m*c*d))

    return answer


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer


n = 10
m = 20

print(solution(n, m))
