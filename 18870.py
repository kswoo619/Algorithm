input()
N = list(map(int, input().split()))
res = []

x = list(set(N))
x.sort()

d = dict(zip(x, [i for i in range(len(x))]))

res = [d[i] for i in N]

print(*res, sep = ' ')
