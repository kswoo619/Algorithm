from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])

    queue = deque()
    queue.append([0, 0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    maps[nx][ny] = maps[x][y] + 1
    
    return maps[N - 1][M - 1] if visited[N - 1][M - 1] else -1