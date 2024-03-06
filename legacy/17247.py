N, M = map(int, input().split())

a = []

for i in range(N):
    ipt = input().split()
    for j, k in enumerate(ipt):
        if(k == '1'):
            a.append((i, j))
print(abs(a[1][0] - a[0][0]) + abs(a[1][1] - a[0][1]))