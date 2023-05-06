def solution(msg):
    answer = []
    
    d = {}
    last_i = 26
    for i in range(1, 27):
        d[chr(64+i)] = i
    
    i = 0
    while True : 
        if i >= len(msg):
            break
        is_a = False
        for j in range(i+1, len(msg)+1):
            if not msg[i:j] in d :
                is_a = True
                d[msg[i:j]] = last_i+1
                last_i +=1
                break
        if j == len(msg) and not is_a: 
            answer.append(d[msg[i:j]])
            break
        else :
            answer.append(d[msg[i:j-1]])
        i = j-1
        
    return answer