import sys

def print_2차원배열(graph):

    for i in graph :
        for j in i:
            print(j, end=' ')
        print()


def dfs(i, j, graph, graph2, n):
    if i < 0 or i >= n or j < 0 or j >=n :
        return False
    elif graph2[i][j] == 0 or graph2[i][j] == 2 or graph2[i][j] == 3:
        return False
    else :
        graph2[i][j] = 2
        dfs(i+1, j, graph, graph2, n)
        dfs(i, j+1, graph, graph2, n)
        dfs(i-1, j, graph, graph2, n)
        dfs(i, j-1, graph, graph2, n)
        return True

def bfs(graph2, min_dist, n):
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
            if graph2[ii][jj] == 2 :  ## 2가 현재 시작할 섬 
                queue.append((ii, jj))
                graph2[ii][jj] = 3

    while len(queue) >0 :
        ii, jj = queue.popleft()

        if isvalidnumber(ii+1, jj) :
            if graph2[ii+1][jj] >= 2 or dist_graph[ii+1][jj]> 0:
                pass
            elif graph2[ii+1][jj] == 0  :
                queue.append((ii+1, jj))
                dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
            else : 
                # dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 

        if isvalidnumber(ii-1, jj)  :
            if graph2[ii-1][jj] >= 2 or dist_graph[ii-1][jj] > 0: 
                pass
            elif graph2[ii-1][jj] == 0  :
                queue.append((ii-1, jj))
                dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
            else :
                # dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 

        if isvalidnumber(ii, jj+1) :
            if graph2[ii][jj+1] >= 2 or dist_graph[ii][jj+1] > 0: 
                pass
            elif graph2[ii][jj+1] == 0 :
                queue.append((ii, jj+1))
                dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
            else :
                # dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
        if isvalidnumber(ii, jj-1)  :
            if graph2[ii][jj-1] >= 2 or dist_graph[ii][jj-1] > 0: 
                pass
            elif graph2[ii][jj-1] == 0 :
                queue.append((ii, jj-1))
                dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
            else :
                # dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj]  :
                    min_dist = dist_graph[ii][jj] 
    #     print("graph2 1")
    #     print_2차원배열(graph2)
    #     print("graph2 2")
    #     print_2차원배열(graph2)

    print("dist_graph")
    print_2차원배열(dist_graph)
    return min_dist


def bfs1(i, j, graph2):
    from collections import deque
    global count
    q = deque()
    q.append([i, j])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph2[nx][ny] == 1:
                graph2[nx][ny] = 2
                q.append([nx, ny])


if __name__ == '__main__' : 
    n = int(input())

    graph = []
    min_dist = sys.maxsize


    for i in range(n):
        graph.append(list(map(int, input().split())))

    import copy 
    graph2 = copy.deepcopy(graph)

    dist_graph = [[0]*n for i in range(n)]

    for i in range(n): 
        for j in range(n):
            if graph2[i][j] == 1 :
                # dfs(i, j, graph, graph2, n)

                bfs1(i, j, graph2)
                print("graph2 2")
                print_2차원배열(graph2)
                min_dist = bfs(graph2, min_dist, n)
                print("graph2 3")
                print_2차원배열(graph2)

    
    print(min_dist)


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