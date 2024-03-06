T = int(input())

for _ in range(T):
    x, y, z = map(int, input().split())
    mat = [[0 for _ in range(x)] for _ in range(y)]
    for _ in range(z):
        a, b = map(int, input().split())
        mat[b][a] = 1
    print()
    print(*mat, sep = '\n')

