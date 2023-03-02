from collections import deque

n, m, v = map(int, input().split())

mat = deque([[] for _ in range(n + 1)])
for _ in range(m):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)

for i in mat:
    i.sort()

visited = [False] * (n + 1)
def dfs(start):
    visited[start] = True
    print(start, end = ' ')
    for i in mat[start]:
        if visited[i] == False:
            dfs(i)

dfs(v)
print()

visited = [False] * (n + 1)
def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in mat[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

bfs(v)