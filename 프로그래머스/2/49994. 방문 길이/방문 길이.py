def solution(dirs):
    pos = [0, 0]
    move = [0, 0]
    visited = []

    for i in dirs:
        if i == "L" and move[0] - 1 >= -5:
            move[0] -= 1
        elif i == "R" and move[0] + 1 <= 5:
            move[0] += 1
        elif i == "D" and move[1] - 1 >= -5:
            move[1] -= 1
        elif i == "U" and move[1] + 1 <= 5:
            move[1] += 1

        if pos+move not in visited and move+pos not in visited and pos != move:
            visited.append(pos+move)

        pos = move.copy()

    return len(visited)