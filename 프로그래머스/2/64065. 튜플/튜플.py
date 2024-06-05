from collections import Counter
def solution(s):
    ans = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    
    cnt = Counter(s)
    for i in cnt.most_common():
        ans.append(int(i[0]))
        
    return ans