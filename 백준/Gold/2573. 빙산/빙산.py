import copy
from collections import deque

def print_2d(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()

def is_ice() : 
    for i in range(N):
        for j in range(M):
            if area[i][j] > 0 : 
                return True
    return False

def melt():
    global area
    temp_area = copy.deepcopy(area)
    n_ice = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            if area[i][j] > 0 : 
                n_ice +=1
                for n in range(4):
                    ii = i + dy[n]
                    jj = j + dx[n]

                    if ii < 0 or jj < 0 or ii >= N or jj >=M:
                        continue
                    if area[ii][jj] == 0 : 
                        cnt += 1
                if area[i][j] - cnt <= 0 : 
                    temp_area[i][j] = 0
                    n_ice -=1
                else : 
                    temp_area[i][j] = area[i][j] - cnt
    area = temp_area
    return n_ice

def count_iceisland():

    def bfs(i, j):
        
        q = deque([[i, j]])

        while q :
            i, j = q.popleft() 

            for n in range(4):
                ii = i + dy[n]
                jj = j + dx[n]

                if ii < 0 or jj < 0 or ii >=N or jj >= M or v[ii][jj]:
                    continue

                if area[ii][jj] > 0 : 
                    q.append([ii, jj])
                    v[ii][jj] = True


    
    v = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0 
    for i in range(N):
        for j in range(M):
            if area[i][j] > 0 and not v[i][j]:
                bfs(i, j)
                cnt +=1 
    
    return cnt



N, M = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

time = 0
is_notseparate = True
n_ice = 1

while n_ice>0 : 
    n_ice = melt()
    time +=1 

    if count_iceisland() >= 2 : 
        print(time) 
        is_notseparate = False
        break

if is_notseparate : 
    print(0)