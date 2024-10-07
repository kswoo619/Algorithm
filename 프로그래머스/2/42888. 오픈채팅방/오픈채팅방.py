from collections import defaultdict
def solution(record):
    answer = []
    d = defaultdict(str)

    for log in record:
        token = log.split()
        if token[0] != 'Leave':
            d[token[1]] = token[-1]

    for log in record:
        token = log.split()
        if token[0] == 'Enter':
            answer.append(d[token[1]]+'님이 들어왔습니다.')
        elif token[0] == 'Leave':
            answer.append(d[token[1]]+'님이 나갔습니다.')
        else:
            continue
        
    return answer