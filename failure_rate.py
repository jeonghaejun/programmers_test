def solution(N, stages):
    answer = []
    current = len(stages)
    fail = [0] * (N+1)

    for i in range(1, N+1):
        cnt = stages.count(i)
        fail[i] = cnt / current
        current -= cnt
        if current == 0:
            break

    for idx, _ in sorted(enumerate(fail[1:]), key=lambda x: x[1], reverse=True):
        answer.append(idx+1)
    return answer
