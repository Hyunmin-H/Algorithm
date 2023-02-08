def solution(scores):
    import copy
    answer = 0
    cnt_high = 0
    if len(scores) ==1 : 
        return 1
    yongho_score = copy.deepcopy(scores[0])
    scores = sorted(scores[1:], key=lambda x : (-x[0], x[1]))
    
    max_b = 0
    for a, b in scores : 
        if a > yongho_score[0] and b > yongho_score[1] : 
            return -1
        if b >= max_b :
            if a+ b > yongho_score[0]+yongho_score[1]:
                cnt_high+=1
            max_b = b
            
        
        
    
    return cnt_high+1