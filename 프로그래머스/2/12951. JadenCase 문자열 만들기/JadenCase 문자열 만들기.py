def solution(s):
    answer = ''
    
    for i in s:
        if answer:
            if answer[-1] == ' ':
                answer += i.upper()
            else:
                answer += i.lower()
        else:
            if i.isalpha():
                answer += i.upper()
            else:
                answer += i
            
    return answer