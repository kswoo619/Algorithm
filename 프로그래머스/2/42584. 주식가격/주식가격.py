def solution(prices):
    stack = []
    res = [0] * len(prices)

    for i in range(len(prices)):
        for s, idx in stack:
            res[idx] += 1
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        stack.append((prices[i], i))

    return res