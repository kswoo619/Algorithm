def solution(s):
    for _ in s:
        valid = 0
        stack = []
        for i in s:
            if not stack or i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if ( stack[-1] == '[' and i == ']' or
                    stack[-1] == '{' and i == '}' or
                    stack[-1] == '(' and i == ')' ):
                    stack.pop()
                    if not stack:
                        valid += 1
                else:
                    stack.append(i)
        if not stack:
            break
        s = s[1:] + s[0]
    return valid if not stack else 0