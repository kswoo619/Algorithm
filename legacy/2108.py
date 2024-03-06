import sys
from collections import Counter

N = int(input())
data = []

for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))

data.sort()

cnt = Counter(data)
most_cnt = sorted(cnt.most_common(), key = lambda x : x[1], reverse = True)

print( round(sum(data)/N) )
print(data[N//2])
print(most_cnt[1][0] if len(most_cnt) != 1 and most_cnt[0][1] == most_cnt[1][1]
      else most_cnt[0][0])
print(max(data) - min(data))
