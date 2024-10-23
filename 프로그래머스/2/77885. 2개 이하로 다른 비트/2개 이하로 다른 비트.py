def solution(numbers):
    answer = []

    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
            continue
        else:
            nxt = bin(i).replace('b', '0')
            for i in range(len(nxt) - 1, 0, -1):
                if nxt[i] == '0':
                    answer.append(int(nxt[:i] + nxt[i+1] + nxt[i] + nxt[i+2:], base=2))
                    break
    
    return answer