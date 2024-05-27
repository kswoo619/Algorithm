def f(num: int) -> int:
    tmp = 1
    for i in range(1, num+1):
        tmp *= i
    return tmp

def solution(n):
    answer = 0
    
    for i, j in enumerate(range(n, n - n//2-1, -1)):
        answer += f(j) // (f(i) * f(j-i))
        
    return answer % 1234567