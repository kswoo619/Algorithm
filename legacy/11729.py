def hanoi(n, start = 1, end = 3, tmp = 2):
    if(n == 1):
        print(start, end)
    else:
        hanoi(n - 1, start, tmp, end)
        print(start, end)
        hanoi(n - 1, tmp, end, start)

n = int(input())

print(2 ** n - 1)
hanoi(n)
