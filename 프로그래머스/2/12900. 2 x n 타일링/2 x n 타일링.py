from collections import deque
def solution(n):
    ans = deque()
    ans.append(1)
    ans.append(2)
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    for i in range(2, n):
        nxt = (ans[i - 1] + ans[i - 2]) % 1000000007
        ans.append(nxt)
    
    return ans[-1] 