from sys import stdin as rr

N, M = map(int, rr.readline().strip().split())

matA = []
matB = []

for _ in range(N):
    tmp = list(map(int, rr.readline().strip().split()))
    matA.append(tmp)
    
M, K = map(int, rr.readline().strip().split())

for _ in range(M):
    tmp = list(map(int, rr.readline().strip().split()))
    matB.append(tmp)

res = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(K):
            res[i][k] += matA[i][j] * matB[j][k]

for i in res:
    print(*i)
