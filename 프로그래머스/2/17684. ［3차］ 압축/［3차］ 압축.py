from collections import defaultdict
def solution(msg):
    ans = []
    lzw = defaultdict()
    alpha = [chr(i) for i in range(65, 91)]
    for i in range(len(alpha)):
        lzw[alpha[i]] = i + 1
    
    idx = 27
    start, end = 0, 1
    while end < len(msg) + 1:
        w = msg[start:end]
        if w in lzw:
            end += 1
        else:
            ans.append(lzw[w[:-1]])
            lzw[w] = idx
            idx += 1
            start = end - 1
    ans.append(lzw[w])
    
    return ans