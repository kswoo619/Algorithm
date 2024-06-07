from collections import deque
def solution(priorities, location):
    ans = 0
    p = deque(enumerate(priorities))
    
    while p:
        loc, priority = p.popleft()
        if any(priority < i for _, i in p):
            p.append((loc, priority))
        else:
            ans += 1
            if loc == location:
                break
    return ans