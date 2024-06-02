import numpy as np
def solution(arr1, arr2):
    mat1 = np.array(arr1)
    mat2 = np.array(arr2)
    
    answer = np.dot(mat1, mat2)
    return answer.tolist()