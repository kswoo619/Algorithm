from itertools import permutations
def isprime(n):
    if n in {0, 1}:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False        
    return True
def solution(numbers):
    check = set()
    ans = set()
    for i in range(len(numbers) + 1):
        for j in set(permutations(numbers, i)):
            if j:
                tmp = int(''.join(j))
                if isprime(tmp):
                    ans.add(tmp)
    return len(set(ans))