from collections import deque

def solution(maps):
    answer = 0
    
    H = len(maps)
    W = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def bfs(i, j): 
        
        v = [[False for _ in range(W)] for _ in range(H)] 
        dist = [[1 for _ in range(W)] for _ in range(H)]
        
        q = deque([[i, j]])
        
        while q : 
            ii, jj = q.popleft()
            
            for n in range(4):
                iii = ii + dy[n]
                jjj = jj + dx[n]
                
                if iii < 0 or jjj < 0 or iii >= H or jjj >= W or maps[iii][jjj] == 0:
                    continue
                    
                if not v[iii][jjj] : 
                    dist[iii][jjj] = dist[ii][jj] + 1
                    v[iii][jjj] = True
                    q.append([iii, jjj])
        
        if dist[H-1][W-1] == 1 : 
            return -1
        else :
            return dist[H-1][W-1]
        
    
    
    
    
    return bfs(0, 0)   