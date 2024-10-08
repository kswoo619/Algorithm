import re
def make_key(files):
    number = re.compile('\d+')
    token = []

    for i in files:
        tmp = number.split(i)
        token.append([tmp[0].lower()] + number.findall(i) + [tmp[-1]])

    return token

def solution(files):
    tmp = make_key(files)
    files = list(zip(files, tmp))

    files.sort(key = lambda x: int(x[1][1]))
    files.sort(key = lambda x: x[1][0])
    
    return list(map(lambda x: x[0], files))