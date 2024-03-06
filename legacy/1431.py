import sys
import time

item = []
digit_sum = []

N = int(input())

for _ in range(N):
    item.append(sys.stdin.readline().strip())

for i in item:
    tmp = 0
    for j in i:
        try:
            tmp += int(j)
        except:
            tmp += 0
    digit_sum.append(tmp)

item = list(zip(item, digit_sum))
item.sort()
item.sort(key = lambda x : x[1])
item.sort(key = lambda x : len(x[0]))
item, digit_sum = zip(*item)

print(*item, sep = '\n')
