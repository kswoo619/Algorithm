def solution(n, lost, reserve):
    
    j = set(lost) & set(reserve)
    lost = list(set(lost) - j)
    reserve = list(set(reserve) - j)
    
    o = len(reserve)
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
        elif i - 1 in reserve:
            reserve.pop(reserve.index(i - 1))
        elif i + 1 in reserve:
            reserve.pop(reserve.index(i + 1))
    print(reserve)    
    
    tmp = len(lost) - (o - len(reserve))
    return n - tmp