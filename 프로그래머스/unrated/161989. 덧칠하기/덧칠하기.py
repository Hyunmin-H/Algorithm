def solution(n, m, section):
    answer = 1
    
    wall = [0 for _ in range(n+1)]
    remain = m
    for n in section : 
        wall[n] = 1
    
    for i in range(1, n+1):
        if wall[i] : 
            if remain > 0 : 
                remain -= 1
            else : 
                answer += 1
                remain = m-1
        else : 
            remain = max(0, remain-1)
    
    ans2 = 1
    remain = m
    for i in range(n, 0, -1):
        if wall[i] : 
            if remain > 0 : 
                remain -= 1
            else : 
                ans2 += 1
                remain = m-1
        else : 
            remain = max(0, remain-1)
            
    return min(answer, ans2)