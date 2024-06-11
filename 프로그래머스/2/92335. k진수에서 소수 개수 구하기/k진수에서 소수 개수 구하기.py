import re
def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    tmp = ''
    while n != 0:
        tmp += str(n % k)
        n //= k
    
    ptn = re.compile('0+')
    p = ptn.split(tmp[::-1])
    p = list(filter(lambda x: len(x) >= 1, p))
    
    for i in p:
        if isprime(int(i)):
            answer += 1
    
    return answer