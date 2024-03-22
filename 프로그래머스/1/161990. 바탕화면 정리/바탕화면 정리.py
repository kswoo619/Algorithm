def solution(wallpaper):
    coord = set()
    answer = []
    
    for i, j in enumerate(wallpaper):
        if '#' in j:
            coord.add((i, j.find('#')))
            coord.add((i + 1, j.find('#') + 1))
            coord.add((i, len(j) - j[::-1].find('#') - 1))
            coord.add((i + 1, len(j) - j[::-1].find('#')))
        
    answer.append(min(coord, key=lambda x: x[0])[0])
    answer.append(min(coord, key=lambda x: x[1])[1])
    answer.append(max(coord, key=lambda x: x[0])[0])
    answer.append(max(coord, key=lambda x: x[1])[1])
    
    return answer