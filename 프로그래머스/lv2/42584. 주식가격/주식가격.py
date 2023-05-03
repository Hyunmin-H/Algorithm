def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i, p1 in enumerate(prices):
        is_fall = False
        for j in range(i+1, len(prices)):
            
            if p1 > prices[j] : 
                answer[i] = j-i
                is_fall = True
                break
        if not is_fall:
            answer[i] = len(prices)-i-1
    
    return answer