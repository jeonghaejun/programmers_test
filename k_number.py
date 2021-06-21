

def solution(array, commands):
    answer = []

    for i, j, k in commands:
        x = array[int(i-1):int(j)]
        x.sort()
        answer.append(x[int(k-1)])
    return answer


# map, lombda이용 겁나 간략하네

def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))