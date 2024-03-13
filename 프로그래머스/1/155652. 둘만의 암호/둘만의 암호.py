def solution(s, skip, index):
    res = ''
    alpha = [chr(i) for i in range(97, 123)]
    
    for i in skip:
        alpha.remove(i)
        
    for c in s:
        idx = alpha.index(c) + index
        
        if idx >= len(alpha):
            idx %= len(alpha)
            
        res += alpha[idx]
    
    return res