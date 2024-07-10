from itertools import product
def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    res = []

    for i in range(1, len(vowel) + 1):
        res.extend(list(product(vowel, repeat=i)))

    res = list(map(lambda x: ''.join(x), res))
    res.sort()

    return res.index(word) + 1