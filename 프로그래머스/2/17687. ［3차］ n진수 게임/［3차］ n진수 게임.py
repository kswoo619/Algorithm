def convert(n :int, base) -> str:
    d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    ans = ''
    while n != 0:
        tmp = n % base
        if tmp < 10:            
            ans = str(tmp) + ans
        else:
            ans = d[tmp] + ans
        n //= base
    
    return ans

def solution(n, t, m, p):
    num = '0'
    i = 0
    while len(num) < t * m:
        num += convert(i, n)
        i += 1
        
    return num[p-1::m][:t]
        
    
        
        