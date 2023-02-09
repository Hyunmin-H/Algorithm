import heapq
def solution(n, works):
    answer = 0
    if sum(works) < n :
        return 0
    
    works_ = [-w for w in works]
    heapq.heapify(works_)
    
    for i in range(n):
        w = heapq.heappop(works_)
        heapq.heappush(works_, w+1)
        
    
    return sum([w**2 for w in works_])