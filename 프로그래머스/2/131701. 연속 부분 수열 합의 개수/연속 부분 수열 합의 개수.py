def solution(elements):

    ans = []
    for _ in range(len(elements)):
        tmp = 0
        for i in elements:
            tmp += i
            ans.append(tmp)
        
        elements.append(elements.pop(0))
        
    return len(set(ans))