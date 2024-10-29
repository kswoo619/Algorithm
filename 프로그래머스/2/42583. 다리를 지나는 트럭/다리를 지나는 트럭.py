from collections import deque
def solution(bridge_length, weight, truck_weights):
    sec = 0
    wait = deque([[i, 0] for i in truck_weights])
    bridge = deque()

    while True:
        if len(wait) == 0 and len(bridge) == 0:
            break

        sec += 1
        if bridge:
            for i in range(len(bridge)):
                bridge[i][1] += 1
            else:
                if bridge[0][1] >= bridge_length:
                    bridge.popleft()

        if wait and sum([i[0] for i in bridge]) + wait[0][0] <= weight:
            bridge.append(wait.popleft())
    
    return sec
