def solution(n):
    fib = [0, 1]
    
    for i in range(1, n):
        if fib[i]:
            fib.insert(i+1, fib[i-1] + fib[i])
    
    return fib[-1] % 1234567