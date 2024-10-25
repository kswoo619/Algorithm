def isValid(m, n, board):
    box = set()
    for y in range(m-1):
        for x in range(n-1):
            tmp = set()
            tmp.update(board[y][x], board[y][x+1], board[y+1][x], board[y+1][x+1])

            if len(tmp) == 1 and '0' not in tmp:
                box.update(((y ,x), (y ,x+1), (y+1 ,x), (y+1 ,x+1)))
    return box

def drop(m, n, board, box):
    after = []
    for x in range(n):
        tmp = []
        flag = 0
        for y in range(m):
            if (y, x) not in box:
                tmp.append(board[y][x])
            else:
                flag += 1
        tmp = ['0'] * flag + tmp
        after.append(tmp)
    
    after = list(zip(*after))
    return after

def solution(m, n, board):
    answer = 0
    while True:
        box = isValid(m, n, board)
        answer += len(box)

        if box:
            board = drop(m, n, board, box)
        else:
            break

    return answer