def solution(board, moves):
    answer = 0
    stack = []
    
    list = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            if board[j][i] > 0:
                tmp.append(board[j][i])
        
        list.append(tmp)          
    
    for i in moves:
        try:
            get = list[i-1].pop(0)
        except:
            get = 0
        
        stack.append(get)
        
        if len(stack) >= 2 and stack[-2] == stack[-1] and stack[-1] != 0:
            answer += 2
            for _ in range(2):
                stack.pop()
        
    return answer