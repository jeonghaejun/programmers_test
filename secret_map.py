def solution(n, arr1, arr2):
    answer = []
    answer2 = []
    map_1 = []
    map_2 = []

    for x, y in zip(list(map(bin, arr1)), list(map(bin, arr2))):
        map_1.append(x[2:].zfill(n))
        map_2.append(y[2:].zfill(n))

    for x, y in zip(map_1, map_2):
        k = ''
        for index in range(n):
            if x[index] == '0' and y[index] == '0':
                k += '0'
            else:
                k += '1'
        answer.append(k)

    for x in answer:
        x = x.replace('1', '#')
        x = x.replace('0', ' ')
        answer2.append(x)

    return answer2

# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


solution(n, arr1, arr2)
