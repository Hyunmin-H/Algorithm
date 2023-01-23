from collections import deque
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())

    graph[u].append([v, w])

q = []
dist = [300001 for _ in range(V+1)]
v = [False for _ in range(V+1)]

dist[start] = 0
heapq.heappush(q, [0, start])

while q:
    w_u, u = heapq.heappop(q)

    if dist[u] < w_u :
        continue

    for vv, w_v in graph[u] :
        d = w_u + w_v
        if d < dist[vv] : 
            dist[vv] = d 
        # dist[vv] = min(dist[vv], dist[u] + w_v)
            heapq.heappush(q, [dist[vv], vv])
    
for d in range(1, len(dist)) :
    if dist[d] ==  300001 :
        print('INF')
    else :
        print(dist[d])




