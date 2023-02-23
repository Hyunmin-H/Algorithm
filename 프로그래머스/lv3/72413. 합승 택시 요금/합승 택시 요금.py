import heapq
import sys

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    
    def dijkstra(start, end_):
        
        d = [0] * (n+1)
        v = [False] * (n+1)
        q = []
        
        # for end, fare in fare_info[start]:
        #     heapq.heappush(q, [fare, start, end])
        #     d[end] = fare
        heapq.heappush(q, [0, start, start])
        # v[start] = True
        
        while q : 
            fare, start, end = heapq.heappop(q)
            
            if not v[end] or d[start] + fare < d[end] :
                d[end] = d[start] + fare
                v[end] = True
                
                for e, f in fare_info[end] :
                    if not v[e]: 
                        heapq.heappush(q, [f, end, e])
        aa = 0
        for e in end_:
            aa += d[e]
        return aa
    
    def dijkstra2(start, end_):
        q = []
        dist = [1e+9 for _ in range(n+1)]
        v = [False for _ in range(n+1)]

        dist[start] = 0
        heapq.heappush(q, [0, start])

        while q:
            w_u, u = heapq.heappop(q)
            v[u] = True


            for vv, w_v in fare_info[u] :
                d = w_u + w_v
                if d < dist[vv] : 
                    dist[vv] = d 
                # dist[vv] = min(dist[vv], dist[u] + w_v)
                    if not v[vv] :
                        heapq.heappush(q, [dist[vv], vv])
        aa = 0
        for e in end_:
            if dist[e] == 1e+9:
                return 1e+9
            aa += dist[e]
        return aa
        
    fare_info = [[] for _ in range(n+1)]
    
    for c, d, f in fares:
        fare_info[c].append([d, f])
        fare_info[d].append([c, f])
        
    t = dijkstra2(s, [a, b])
    answer = min(answer, t)
    
    for nn in range(1, n+1):
        # print('nn', nn)
        if nn == s : 
            continue
        one = dijkstra2(s, [nn])
        two = dijkstra2(nn, [a, b])
        
        if not one or not two: 
            continue
        # if one > 300000 or two > 300000 :
        #     continue
        answer = min(answer, one+two)
    
    return answer