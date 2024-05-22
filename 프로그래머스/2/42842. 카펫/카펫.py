def solution(brown, yellow):
    div = [(1, yellow)]
    for i in range(2, yellow//2 + 1):
        if yellow % i == 0:
            div.append((i, yellow//i))
            
    for i in div:
        x = i[0] + 2
        y = i[1] + 2
        if x * y - yellow == brown:
            return [max(x, y), min(x, y)]
    
    return div