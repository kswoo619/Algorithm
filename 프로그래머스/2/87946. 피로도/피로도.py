from itertools import permutations
def solution(k, dungeons):
    ans = []
    for d in permutations(dungeons, len(dungeons)):
        l = k
        tmp = 0
        for i in d:
            if l >= i[0]:
                l -= i[1]
                tmp += 1
        ans.append(tmp)

    return max(ans)