import sys

N, M = list(map(int, input().split()))
data = list(map(int, input().split()))
test = []
acc = [0] * (N + 1)

for _ in range(M):
    test.append(sys.stdin.readline().strip())

for i in range(1, N + 1):
    acc[i] = acc[i - 1] + data[i - 1]

for t in test:
    x, y = t.split()
    print(acc[int(y)] - acc[int(x) - 1])
