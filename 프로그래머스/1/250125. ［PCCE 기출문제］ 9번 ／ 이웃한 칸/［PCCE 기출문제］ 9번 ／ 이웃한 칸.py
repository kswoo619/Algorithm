def solution(board, h, w):
    target = board[h][w]
    res = 0
    length = len(board)
    
    if h-1 >= 0 and board[h-1][w] == target:
        res += 1
    
    if h+1 <= length - 1 and board[h+1][w] == target:
        res += 1
        
    if w-1 >= 0 and board[h][w-1] == target:
        res += 1
    
    if w+1 <= length - 1 and board[h][w+1] == target:
        res += 1
    
    return res