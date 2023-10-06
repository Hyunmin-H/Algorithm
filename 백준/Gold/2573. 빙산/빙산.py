import copy
import sys
sys.setrecursionlimit(10**4)


def print_2d(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()

def melt_ice():
    global area
    new_ice = copy.deepcopy(area)

    for i in range(N):
        for j in range(M):
            num = 0
            for n in range(4):
                ii = i + dy[n]
                jj = j + dx[n]

                if ii < 0 or jj < 0 or ii > N-1 or jj > M-1 :
                    continue

                if area[ii][jj] == 0 :
                    num +=1
            new_ice[i][j] = max(0, new_ice[i][j] - num)
    area = new_ice
    # return new_ice

def calc_iceNum():

    v = [[0 for _ in range(M)] for _ in range(N)]
    num_ice = 0
    is_ice = False
    for i in range(N):
        for j in range(M):
            if area[i][j] > 0 and v[i][j] == 0:
                num_ice += 1
                dfs(i, j, v)
                is_ice = True
    
    if not is_ice : 
        return False
    return num_ice

def dfs(i, j, v):
    if i < 0 or j < 0 or i > N-1 or j > M-1 or v[i][j] != 0 :
        return
    else :
        v[i][j] = 1
        for n in range(4):
            ii = i + dy[n]
            jj = j + dx[n]

            if v[ii][jj] == 0 and area[ii][jj] > 0 :
                dfs(ii, jj, v)

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

time = 0
while True :
    time +=1

    melt_ice()
    n = calc_iceNum()
    if n is False :
        print(0)
        exit()
    if n >= 2 :
        break

print(time )