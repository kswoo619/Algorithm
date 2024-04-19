def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack:
            if stack[-1] == '(' and i == ')':
                stack.pop(-1)
            else:
                stack.append(i)
            
    return True if not stack else False