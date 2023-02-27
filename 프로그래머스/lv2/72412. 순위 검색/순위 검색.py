import bisect
import numpy as np
from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = {}
    scores = []
    
    for i, s in enumerate(info):
        lg, fb, js, cp, score = s.split(' ')
        
        info_names = [lg, fb, js, cp]
        for j in range(5):  
            for c in combinations(info_names, j):
                temp = ''.join(c)
                if temp in info_dict:
                    info_dict[temp].append(int(score))  
                else:
                    info_dict[temp] = [int(score)]
    
    for value in info_dict.values():
        value.sort()
    
    
    for s in query:
        lg, fb, js, cp_ = s.split(' and ')
        cp, score = cp_.split(' ')
        score = int(score)
        
        info_names = [lg, fb, js, cp]
        ans_name = ''
        for name in info_names : 
            if name != '-':
                ans_name += name
        
        if ans_name in info_dict : 
            tmp = info_dict[ans_name]
        else : 
            answer.append(0)
            continue
        
        idx = bisect.bisect_left(tmp, score)
        # answer.append(len(tmp[idx:]))
        answer.append(len(tmp) - idx)
        
    
    return answer