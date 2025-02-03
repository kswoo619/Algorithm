def solution(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        res.append(list(map(lambda x, y: x+y, arr1[i], arr2[i])))
    
    return res