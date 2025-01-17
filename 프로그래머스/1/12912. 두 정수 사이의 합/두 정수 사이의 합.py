def solution(a, b):
    if a == b:
        return a
    
    if a > b:
        # t = [i for i in range(a, b - 1, -1)]
        return sum([i for i in range(b, a+1)])
    else:
        # t = [i for i in range(a, b + 1)]
        return sum([i for i in range(a, b+1)])
    # return sum(t)