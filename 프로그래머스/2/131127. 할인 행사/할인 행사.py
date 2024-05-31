from collections import Counter
def solution(want, number, discount):
    answer = 0
    myd = dict(zip(want, number))
    
    n = sum(number)
    cnt = Counter(discount[:n])
    
    if myd.items() == cnt.items():
            answer += 1
    
    for i, j in enumerate(range(n, len(discount))):
        cnt[discount[i]] -= 1
        cnt[discount[j]] += 1
        if cnt[discount[i]] == 0:
            del cnt[discount[i]]
        
        if myd.items() == cnt.items():
            answer += 1
        
    return answer