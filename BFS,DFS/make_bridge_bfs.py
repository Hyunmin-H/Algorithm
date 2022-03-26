def print_2차원배열(graph):

    for i in graph :
        for j in i:
            print(j, end=' ')
        print()

def dfs(i, j, graph, graph2, n):
    if i < 0 or i >= n or j < 0 or j >=n :
        return False
    elif graph2[i][j] == 0 or graph2[i][j] == 2:
        return False
    else :
        graph2[i][j] = 2
        dfs(i+1, j, graph, graph2, n)
        dfs(i, j+1, graph, graph2, n)
        dfs(i-1, j, graph, graph2, n)
        dfs(i, j-1, graph, graph2, n)
        return True

def bfs(i, j, graph2, dist_graph, min_dist):
    from collections import deque

    queue = deque()
    queue.append((i, j))

    def isvalidnumber(ii, jj):
        if ii < 0 or ii >= n or jj < 0 or jj >=n :
            return False
        else : 
            return True


    while len(queue) >0 :
        ii, jj = queue.popleft()

        if isvalidnumber(ii+1, jj) :
            if graph2[ii+1][jj] == 2 or dist_graph[ii+1][jj]> 0:
                pass
            elif graph2[ii+1][jj] == 0  :
                queue.append((ii+1, jj))
                dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
            else :
                dist_graph[ii+1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj] + 1 :
                    min_dist = dist_graph[ii][jj] + 1

        if isvalidnumber(ii-1, jj)  :
            if graph2[ii-1][jj] == 2 or dist_graph[ii-1][jj] > 0: 
                pass
            elif graph2[ii-1][jj] == 0  :
                queue.append((ii-1, jj))
                dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
            else :
                dist_graph[ii-1][jj] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj] + 1 :
                    min_dist = dist_graph[ii][jj] + 1

        if isvalidnumber(ii, jj+1) :
            if graph2[ii][jj+1] == 2 or dist_graph[ii][jj+1] > 0: 
                pass
            elif graph2[ii][jj+1] == 0 :
                queue.append((ii, jj+1))
                dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
            else :
                dist_graph[ii][jj+1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj] + 1 :
                    min_dist = dist_graph[ii][jj] + 1
        if isvalidnumber(ii, jj-1)  :
            if graph2[ii][jj-1] == 2 or dist_graph[ii][jj-1] > 0: 
                pass
            elif graph2[ii][jj-1] == 0 :
                queue.append((ii, jj-1))
                dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
            else :
                dist_graph[ii][jj-1] = dist_graph[ii][jj] + 1
                if min_dist > dist_graph[ii][jj] + 1 :
                    min_dist = dist_graph[ii][jj] + 1
    return min_dist


if __name__ == '__main__' : 
    n = int(input())

    graph = []
    min_dist = 20


    for i in range(n):
        graph.append(list(map(int, input().split())))

    
    
    import copy 
    graph2 = copy.deepcopy(graph)

    for i in range(n): 
        for j in range(n):
            if graph2[i][j] == 1 :
                dfs(i, j, graph, graph2, n)

                # for ii in range(n): 
                #     for jj in range(n):
            elif graph2[i][j] ==2 : 
                dist_graph = [[0]*n for i in range(n)]
                min_dist = bfs(i, j, graph2, dist_graph, min_dist)
                # print("dist_graph")
                # print_2차원배열(dist_graph)
                del dist_graph
                
                # print("graph22")
                # print_2차원배열(graph2)
                
                # for ii in range(n): 
                #     for jj in range(n):
                #         if graph2[ii][jj] ==2 : 
                #             graph2[ii][jj] = 3

    
    print(min_dist-1)
