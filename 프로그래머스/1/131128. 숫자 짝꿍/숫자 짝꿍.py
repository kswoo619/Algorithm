from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    tmp = ''
    
    inter = list(set(x.keys() & set(y.keys())))
    
    for i in inter:
        tmp += i * min(x[i], y[i])
    
    if set(inter) == {'0'}:
        tmp = '0'
    
    tmp = ''.join(sorted(tmp, reverse=True))
    
    return tmp if inter else '-1'