import sys
sys.setrecursionlimit(10**7)


def print_2차원배열(graph):

    for i in graph :
        for j in i:
            print(j, end=' ')
        print()


def dfs(i, j, graph, graph2, cnt):
    if i < 0 or i >= n or j < 0 or j >=n :
        return False
    elif graph2[i][j] > 0 or graph[i][j] == 0 : #graph2[i][j] == 0 or graph2[i][j] == 2 or graph2[i][j] == 3:
        return False
    else :
        graph2[i][j] = cnt
        dfs(i+1, j, graph, graph2, cnt)
        dfs(i, j+1, graph, graph2, cnt)
        dfs(i-1, j, graph, graph2, cnt)
        dfs(i, j-1, graph, graph2, cnt)
        return True

def bfs(graph2, min_dist, cnt):
    from collections import deque

    dist_graph = [[0]*n for _ in range(n)]

    queue = deque()

    def isvalidnumber(ii, jj):
        if ii < 0 or ii >= n or jj < 0 or jj >=n :
            return False
        else : 
            return True

    for ii in range(n):
        for jj in range(n):
            if graph2[ii][jj] == cnt :  
                queue.append((ii, jj))

    while queue :
        ii, jj = queue.popleft()

        # if ii+1 >= 0 and ii+1 < n and jj >= 0 and jj <n:  #isvalidnumber(ii+1, jj) :
        if isvalidnumber(ii+1, jj) :
            if graph2[ii+1][jj] == cnt or dist_graph[ii+1][jj]> 0:
                pass
            elif graph2[ii+1][jj] == -1  :
                queue.append((ii+1, jj))
                dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
            elif graph2[ii+1][jj] >0: 
                # dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
                    return min_dist

        # if ii-1 >= 0 and ii-1 < n and jj >= 0 and jj <n:  #isvalidnumber(ii-1, jj)  :
        if isvalidnumber(ii-1, jj)  :
            if graph2[ii-1][jj] == cnt or dist_graph[ii-1][jj] > 0: 
                pass
            elif graph2[ii-1][jj] == -1  :
                queue.append((ii-1, jj))
                dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
            elif graph2[ii-1][jj] >0: 
                # dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
                    return min_dist

        # if ii >= 0 and ii < n and jj+1 >= 0 and jj+1 <n:  #isvalidnumber(ii, jj+1) :
        if isvalidnumber(ii, jj+1) :
            if graph2[ii][jj+1] == cnt or dist_graph[ii][jj+1] > 0: 
                pass
            elif graph2[ii][jj+1] == -1 :
                queue.append((ii, jj+1))
                dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
            elif graph2[ii][jj+1] >0: 
                # dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
                    return min_dist

        # if ii >= 0 and ii < n and jj-1 >= 0 and jj-1 <n:  #isvalidnumber(ii, jj-1)  :
        if isvalidnumber(ii, jj-1)  :
            if graph2[ii][jj-1] == cnt or dist_graph[ii][jj-1] > 0: 
                pass
            elif graph2[ii][jj-1] == -1 :
                queue.append((ii, jj-1))
                dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
            elif graph2[ii][jj-1] >0: 
                # dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
                    return min_dist


    
    for ii in range(n):
        for jj in range(n):
            if graph2[ii][jj] == 2 :  ## 2가 현재 시작할 섬 
                graph2[ii][jj] = 3
    #     print("graph2 1")
    #     print_2차원배열(graph2)
    #     print("graph2 2")
    #     print_2차원배열(graph2)

    # print("dist_graph")
    # print_2차원배열(dist_graph)
    return min_dist


def bfs1(i, j, graph2, cnt, graph):
    from collections import deque
    q = deque()
    q.append([i, j])
    graph2[i][j] = cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph2[nx][ny] == -1 and graph[nx][ny] == 1:
                graph2[nx][ny] = cnt
                q.append([nx, ny])


n = int(input())

graph = []
min_dist = sys.maxsize


for i in range(n):
    graph.append(list(map(int, input().split())))

import copy 
# graph2 = copy.deepcopy(graph)

import time

t = time.time()
graph2 = [[-1]*n for i in range(n)]
count_island = 0
for i in range(n): 
    for j in range(n):
        if graph[i][j] == 1 and graph2[i][j] ==-1:
            count_island +=1     
            dfs(i, j, graph, graph2, count_island)
            # bfs1(i, j, graph2, count_island, graph)
            # print("graph2 2")
            # print_2차원배열(graph2)

# print("graph2")
# print_2차원배열(graph2)

# print("time1:",  t1 - t)
# print("graph2")
# print_2차원배열(graph2)

for i in range(1,count_island):
    min_dist = bfs(graph2, min_dist, i)
print(min_dist)

# print("time2:", time.time() - t1)

'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''