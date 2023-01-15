import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    
    np1 = np.array(arr1)
    np2 = np.array(arr2)
    
    print(np1+np2)
    
    
    return (np1+np2).tolist()