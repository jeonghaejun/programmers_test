

def solution(arr1, arr2):
    for x in range(len(arr1)):
        for y in range(len(arr1[0])):
            arr1[x][y] += arr2[x][y]
    return arr1


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))
