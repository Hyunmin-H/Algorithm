import copy
import sys
sys.setrecursionlimit(10**6)

def DFS(v):
    visited[v] = True
    for vv in graph[v]:
        if visited[vv]:
            continue
        DFS(vv)

    stack.append(v)

def DFS2(v, first):
    visited2[v] = True

    for vv in graph_r[v]:
        # if vv == first :
        #     return
        if visited2[vv] : 
            continue
        scc.add(vv)
        DFS2(vv, first)

input = sys.stdin.readline
V, E = map(int, input().split())

graph = [[] for i in range(V+1)]
graph_r = [[] for i in range(V+1)]

for i in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph_r[v2].append(v1)

visited = [False for i in range(V+1)]
stack = []
SCCs = []

for v in range(1, V+1):
    if visited[v]:
        continue
    DFS(v)
# print('visited', visited)

visited2 = [False for i in range(V+1)]
# print('stack', stack)

while stack:
    v = stack.pop()
    if visited2[v]:
        continue
    scc = set({v})
    DFS2(v, v)

    scc = list(scc)
    scc = sorted(scc)
    scc.append(-1)
    SCCs.append(scc)

    # print('stack', stack)
SCCs = sorted(SCCs)

print(len(SCCs))
for scc in SCCs:
    for j in range(len(scc)):
        if j == len(scc)-1:
            print(scc[j])
        else :
            print(scc[j], end=' ')

'''
7 9
1 4
4 5
5 1
1 6
6 7
2 7
7 3
3 7
7 2

out 
3
1 4 5 -1
2 3 7 -1
6 -1
'''

'''
11 16
1 4
4 5
5 6
6 7
7 5
4 6
1 3
3 2
2 8
8 10
10 11
11 8
8 9
9 5
2 1
9 10

out
4
1 2 3 -1
4 -1
5 6 7 -1
8 9 10 11 -1

'''

'''
11 17
1 4
4 5
5 6
6 7
7 5
4 6
1 3
3 2
2 8
8 10
10 11
11 10
10 8
8 9
9 5
2 1
9 11

out 
4
1 2 3 -1
4 -1
5 6 7 -1
8 9 10 11 -1

'''

'''
4 5
1 4
2 4
3 4
4 1
4 2

out
2
1 2 4 -1
3 -1

'''