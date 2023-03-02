import sys
from collections import deque

ans = 0
N = int(input())
test = deque()
stack = deque()

for _ in range(N):
    test += sys.stdin.readline().split()

for t in test:
    stack.clear()
    for i, j in enumerate(t):
        if(len(stack) == 0):
            stack.append(j)
        else:
            if(stack[-1] != j):
                stack.append(j)
            else:
                stack.pop()
    if(len(stack) == 0):
        ans += 1
            
print(ans)
