def solution(n, left, right):
    answer = [i for i in range(left, right+1)]
    answer = list(map(lambda x: max(x // n, x % n) + 1, answer))
    
    return answer