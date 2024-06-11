def solution(numbers, target):
    def dfs(s, idx):
        global ans
        if idx == len(numbers):
            if s == target:
                ans += 1
            return
        
        dfs(s + numbers[idx], idx + 1)
        dfs(s - numbers[idx], idx + 1)
    
    global ans
    ans = 0
    dfs(0, 0) 
    return ans
        