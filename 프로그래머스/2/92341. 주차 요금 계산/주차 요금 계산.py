from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    d = defaultdict(int)
    
    for info in records:
        tmp = info.split()
        if tmp[2] == 'IN':
            d[tmp[1]] -= int(tmp[0][:2]) * 60 + int(tmp[0][3:])
        else:
            d[tmp[1]] += int(tmp[0][:2]) * 60 + int(tmp[0][3:])
    
    k = list(d.keys())
    k.sort()
    
    for i in k:
        if d[i] <= 0:
            d[i] += 23 * 60 + 59
        
        if d[i] <= fees[0]:
            answer.append(fees[1])
        else:
            money = fees[1] + math.ceil((d[i] - fees[0]) / fees[2]) * fees[3]
            answer.append(money)
     
    return answer