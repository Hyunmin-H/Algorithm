from collections import deque
def solution(queue1, queue2):
    answer = -2

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    n = len(q1) + len(q2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if abs(sum1 - sum2) % 2 != 0:
        return -1
    diff = sum1 - sum2
    
    cnt = 0
    if diff == 0 :
        return 0
    
    while q1 and q2 : 
        if cnt > 2*n :
            return -1
        if diff < 0 : 
            t = q2.popleft()
            q1.append(t)
            sum1 += t
            sum2 -= t
            diff += 2*t
            cnt += 1
        elif diff > 0 : 
            t = q1.popleft()
            q2.append(t)
            sum1 -= t
            sum2 += t

            diff -= 2*t
            cnt += 1
        
        if diff == 0 : 
            return cnt
  
    return -1