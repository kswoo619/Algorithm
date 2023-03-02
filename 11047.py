import sys

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().strip()))

res = 0
while(K != 0):
    for item in coin[::-1]:
        res += K // item
        K %= item

print(res)
