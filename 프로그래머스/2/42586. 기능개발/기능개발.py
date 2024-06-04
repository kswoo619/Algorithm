from math import ceil
def solution(progresses, speeds):
    finish = []
    ans = []
    for i, j in zip(progresses, speeds):
        finish.append(ceil((100 - i) / j))
    
    max = -1
    for i in range(len(finish)):
        if not ans:
            ans.append(1)
        else:
            if finish[i] <= max:
                ans[-1] += 1
            else:
                max = finish[i]
                ans.append(1)            
        
        if max < finish[i]:
            max = finish[i]
                
    return ans