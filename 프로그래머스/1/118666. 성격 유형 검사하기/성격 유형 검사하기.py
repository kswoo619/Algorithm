def solution(survey, choices):
    ktype = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = [3, 2, 1, 0, 1, 2, 3]
    
    for i, j in enumerate(choices):
        if j >= 5:
            ktype[survey[i][-1]] += score[j - 1]
        else:
            ktype[survey[i][0]] += score[j - 1]
        
    answer = ''
            
    for i in ['RT', 'CF', 'JM', 'AN']:
        answer += max(i, key=ktype.get)
    
    return answer