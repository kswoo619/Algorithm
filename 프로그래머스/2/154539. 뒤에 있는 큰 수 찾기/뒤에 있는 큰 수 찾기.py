from collections import deque

def solution(numbers):

    n = len(numbers)
    answer = [-1] * n

    stack = deque()
    stack.append(0)

    for i in range(1, n):
        num = numbers[i]
        while stack:
            if numbers[stack[-1]] < num:
                answer[stack.pop()] = num
            else:
                break
        stack.append(i)

    return answer