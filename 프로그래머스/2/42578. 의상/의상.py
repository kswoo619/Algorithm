from collections import defaultdict
def solution(clothes):
    ans = 1
    option = defaultdict(list)
    
    for i, j in clothes:
        option[j].append(i)        
    
    for i in option.values():
        ans *= len(i) + 1
        
    return ans - 1