from collections import Counter
def solution(topping):
    res = 0
    right = Counter(topping)
    left = set()
    for i in topping:
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        left.add(i)
        if len(right) == len(left):
            res += 1

    return res