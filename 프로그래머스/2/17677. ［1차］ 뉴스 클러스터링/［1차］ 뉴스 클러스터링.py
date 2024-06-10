def solution(str1, str2):
    set1 = []
    set2 = []
    

    for i in range(len(str1) - 1):
        set1.append(str1[i:i+2].lower())
    
    for i in range(len(str2) - 1):
        set2.append(str2[i:i+2].lower())
    
    set1 = list(filter(lambda x: x.isalpha(), set1))
    set2 = list(filter(lambda x: x.isalpha(), set2))
    
    u = d = 0
    for i in set(set1)|set(set2):
        d += max(set1.count(i), set2.count(i))
        u += min(set1.count(i), set2.count(i))
    
    return int((u / d) * 65536) if d != 0 else 65536