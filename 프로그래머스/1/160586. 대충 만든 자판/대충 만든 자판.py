def solution(keymap, targets):
    res = []
    
    for target in targets:
        tmp = 0
        for i in target:
            idx = list(map(lambda x: x.find(i), keymap))
            
            if set(idx) == {-1}:
                tmp = -1
                break
            else:
                tmp += min(filter(lambda x: x >= 0, idx)) + 1
        res.append(tmp)
    return res
                