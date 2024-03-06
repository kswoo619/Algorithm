N = int(input())

test = []

for _ in range(N):
    test.append(int(input()))

for n in test:
    if(n != 0 and n != 1):
        f = [0] * (n + 1)

        f[0] = (1, 0)
        f[1] = (0, 1)

        for i in range(2, n + 1):
            a = f[i - 1][0] + f[i - 2][0]
            b = f[i - 1][1] + f[i - 2][1]
            f[i] = (a, b)

        print(*f[-1])
    else:
        print('1 0' if n == 0 else '0 1')
