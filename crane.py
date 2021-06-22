def solution(board, moves):
    result = 0
    box = []
    for move in moves:
        move = move-1
        for x in range(len(board)):
            if board[x][move] != 0:
                box.append(board[x][move])
                board[x][move] = 0

                if len(box) >= 2:
                    if box[-1] == box[-2]:
                        del box[-1]
                        del box[-1]
                        result += 2
                break

    return result


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
