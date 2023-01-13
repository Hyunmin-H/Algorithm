def solution(brown, yellow):
    answer = []
    
    w_plus_h = (brown -4)//2
    print(w_plus_h)
    print((w_plus_h) // 2)
    
    for h in range(1, (w_plus_h) // 2+1):
        w = w_plus_h - h
        print(w, h)
        if w*h == yellow : 
            return [w+2, h+2]
    
    return answer