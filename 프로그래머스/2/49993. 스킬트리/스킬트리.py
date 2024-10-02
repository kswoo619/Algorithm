def solution(skill, skill_trees):
    idx = dict(zip([skill[i] for i in range(len(skill))], [i for i in range(len(skill))]))
    answer = 0

    for tree in skill_trees:
        tmp = []
        for i in tree:
            if i in skill:
                tmp.append(idx[i])

        if tmp == [i for i in range(len(tmp))]:
            answer += 1

    return answer