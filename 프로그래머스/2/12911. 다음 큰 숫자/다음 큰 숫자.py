def solution(n):
    one = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == one:
            return n
        