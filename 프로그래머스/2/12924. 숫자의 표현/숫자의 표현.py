def solution(n):
    div = set([1, n])
    for i in range(2, n//2 + 1):
        if n % i == 0:
            div.add(i)
    
    return len(list(filter(lambda x: x % 2 != 0, div)))