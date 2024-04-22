def solution(s):
    zero = 0
    i = 0
    
    while s != '1':
        i += 1
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
    
    answer = [i, zero]
    
    return answer