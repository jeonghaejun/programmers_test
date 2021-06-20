

def solution(array, commands):
    answer = []
    x = []
    for i, j, k in commands:

        if i != j:
            x = array[int(i-1):int(j-1)]
            print(x)
        else:
            x = array[int(i-1)]
            print(x)

    #     y=x.sort()
    #     y = x[int(k-1)]
    #     # print(y)
    #     answer.append(y)
    # return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)
