from collections import deque

def solution(maps):
    answer = 0
    
    H = len(maps)
    W = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def bfs(i_, j_): 
        
        v = [[False for _ in range(W)] for _ in range(H)] 
        dist = [[1 for _ in range(W)] for _ in range(H)]
        
        q = deque([[i_, j_]])
        
        while q : 
            i, j = q.popleft()
            
            for n in range(4):
                ii = i + dy[n]
                jj = j + dx[n]
                
                if ii < 0 or jj < 0 or ii >= H or jj >= W or maps[ii][jj] == 0:
                    continue
                    
                if not v[ii][jj] : 
                    dist[ii][jj] = dist[i][j] + 1
                    v[ii][jj] = True
                    q.append([ii, jj])
        
        if dist[H-1][W-1] == 1 : 
            return -1
        else :
            return dist[H-1][W-1]
        
    
    
    
    
    return bfs(0, 0)   