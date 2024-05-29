from collections import Counter
def solution(k, tangerine):
    answer = []
    cnt = Counter(tangerine)
    for i, j in cnt.most_common():
        k -= j
        answer.append(i)
        if k <= 0:
            break
    
    return len(answer)