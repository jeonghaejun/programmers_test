def solution(answers):
    score = []
    people = []
    x1 = [1, 2, 3, 4, 5]
    x2 = [2, 1, 2, 3, 2, 4, 2, 5]
    x3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0

    for index, ans in enumerate(answers):
        if ans == x1[index % 5]:
            count1 += 1
        if ans == x2[index % 8]:
            count2 += 1
        if ans == x3[index % 10]:
            count3 += 1
        
    score.extend([count1,count2,count3])

    for index, x in enumerate(score):
        if x == max(score):
            people.append(index+1)
    
    return people

# 다른사람 풀이

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


answers = [1, 3, 2, 4, 2]

print(solution(answers))
