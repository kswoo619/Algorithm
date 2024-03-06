tog = {0 : 1, 1 : 0}

int(input())
state = list(map(int, input().split()))
N = input()
task = []
for _ in range(int(N)):
    task += map(int, input().split())

for i in range(0, len(task), 2):
    tmp = task[i + 1]
    if(task[i] == 1):
        for j in range(tmp - 1, len(state), tmp):
            state[j] = tog[state[j]]
    else:
        j = 1
        tmp -= 1
        state[tmp] = tog[state[tmp]]
        while True:
            try:
                if(state[tmp + j] == state[tmp - j]) and tmp + j <= len(state) and tmp - j >= 0:
                    state[tmp + j] = tog[state[tmp + j]]
                    state[tmp - j] = tog[state[tmp - j]]
                    j += 1
                else:
                    break
            except:
                break

while(state):
    print(*state[:20], sep = ' ')
    state = state[20:]
