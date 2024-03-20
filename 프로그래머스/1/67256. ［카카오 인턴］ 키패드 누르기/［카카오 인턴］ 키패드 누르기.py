def solution(numbers, hand):
    
    def distance(a, b):
        tmp = abs(getDict[a][0] - getDict[b][0]) + abs(getDict[a][1] - getDict[b][1])
        return tmp if tmp > 0 else -tmp
    
    coord = [(i, j) for i in range(4) for j in range(3)]
    char = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
    getDict = dict(zip(char, coord))
    
    answer = ''
    
    lpos = '*'
    rpos = '#'
    for i in numbers:
        if i in (1, 4, 7, '*'):
            answer += 'L'
        elif i in (3, 6, 9, '#'):
            answer += 'R'
        else:
            if distance(lpos, i) > distance(rpos, i):
                answer += 'R'
            elif distance(lpos, i) < distance(rpos, i):
                answer += 'L'
            else:
                if hand == 'right':
                    answer += 'R'
                else:
                    answer += 'L'
                    
        if answer[-1] == 'L':
            lpos = i
        else:
            rpos = i
                    
    return answer     