import sys
from collections import deque

N = int(input())
stack = deque()

for _ in range(N):
    tmp = int(sys.stdin.readline().strip())
    if(tmp == 0):
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))
