from collections import deque

hungry = deque(map(int, input().split()))
ticket = deque(map(int, input().split()))

full = 0

for _ in range(5):
    if(hungry[0] > ticket[0]):
        full += ticket[0]
        hungry[0] -= ticket[0]
        ticket[0] = 0
       
    else:
        full += hungry[0]
        ticket[0] -= hungry[0]
        hungry[0] = 0

        event = ticket[0] // 3
        ticket[0] -= event * 3
        ticket[1] += event

    hungry.rotate(-1)
    ticket.rotate(-1)  

print(full)
