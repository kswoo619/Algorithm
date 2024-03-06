import sys
from collections import deque

T = int(input())
test = deque()
docs = deque()

for _ in range(T * 2):
    test.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, len(test), 2):
    tmp_idx = test[i - 1][-1]
    tmp = [0 if j != tmp_idx else 1 for j in range(len(test[i]))]
    docs.append(list(zip(test[i], tmp)))

for doc in docs:
    res = 1
    tmp = deque(doc)
    Xmax = sorted(tmp, key = lambda x: x[0], reverse = True)[0]

    while(Xmax[-1] != 1):
        Xmax = sorted(tmp, key = lambda x: x[0], reverse = True)[0]
        for _ in range(tmp.index(Xmax)):
            tmp.append(tmp.popleft())
        item = tmp.popleft()
        if(item[-1] == 1):
            break
        
        res += 1

    print(res)
