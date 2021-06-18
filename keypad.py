def distance(number,hand):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    hand_index,num_index=None,None
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == hand:
                hand_index = (i,j)
            if keypad[i][j] == number:
                num_index=(i,j)
    return abs(hand_index[0]-num_index[0])+abs(hand_index[1]-num_index[1])

def solution(numbers, hand):
    answer = ''
    left,right='*','#'
    for number in numbers:
        if number in [1,4,7]:
            answer+='L'
            left=number
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        else:
            if distance(number,left)<distance(number,right):
                answer += 'L'
                left=number
            elif distance(number,left)>distance(number,right):
                answer += 'R'
                right = number
            else:
                if hand == 'right':
                    answer +='R'
                    right = number
                else:
                    answer += 'L'
                    left = number
    return answer