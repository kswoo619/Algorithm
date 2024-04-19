def solution(s):
    answer = ""
    n = list(map(int, s.split()))
    answer += str(min(n))
    answer += ' '
    answer += str(max(n))
    
    return answer