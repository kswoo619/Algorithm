from collections import deque
def solution(order):
    stack = deque()
    idx = 0

    for i in range(1, len(order) + 1):
        stack.append(i)
        
        if stack[-1] == order[idx]:
            while stack and stack[-1] == order[idx]:
                idx += 1
                stack.pop()
        else:
            continue
        
    return idx