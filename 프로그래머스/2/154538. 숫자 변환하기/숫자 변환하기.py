from collections import deque

def makecase(x, y, n):
    queue = deque()
    queue.append((y, 0))
    
    while queue:
        curr = queue.popleft()
        times = curr[1] + 1
        
        if curr[0] > x:
            if curr[0] % 3 == 0:
                queue.append((curr[0] // 3, times))
            if curr[0] % 2 == 0:
                queue.append((curr[0] // 2, times))
            queue.append((curr[0] - n, times))
        
        elif curr[0] == x:
            return times - 1
    return -1
    
def solution(x, y, n):
    return makecase(x, y, n)