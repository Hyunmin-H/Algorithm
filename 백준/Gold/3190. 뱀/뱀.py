
N = int(input())
K = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

for k in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

L = int(input())
dir = [0] * 10000
for l in range(L):
    i, d = input().split()
    dir[int(i)] = d

def print_2d(a):
    for i in a :
        for j in i:
            print(j, end=' ')
        print()

def move_end(i_e, j_e):
    d = dir_2d[i_e][j_e]
    return i_e + dy[d], j_e + dx[d]
def move(i_s, j_s, i_e, j_e, d):
    ## 앞 블록이 벽이나 몸인지 확인
    ii = i_s + dy[d]
    jj = j_s + dx[d]
    if ii < 0 or jj < 0 or ii >=N or jj >=N :
        return False, 0, 0, 0, 0

    if arr[ii][jj] == 2 :
        return False, 0, 0, 0, 0

    ## 사과일 경우
    elif arr[ii][jj] == 1 :
        arr[ii][jj] = 2
        dir_2d[i_s][j_s] = d
    else : ## 0일 경우
        arr[ii][jj] = 2
        dir_2d[i_s][j_s] = d
        arr[i_e][j_e] = 0
        i_e, j_e = move_end(i_e, j_e)

    return True, ii, jj, i_e, j_e




    ## 사과가 있는지 확인
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

time = 0
d = 0
i_s, j_s = [0, 0]
i_e, j_e = [0, 0]
arr[0][0] = 2
dir_2d = [[0 for _ in range(N)] for _ in range(N)]

while(1):
    if dir[time] =='L':
        d = (d-1) % 4
    elif dir[time] == 'D':
        d = (d+1) % 4
    is_moved, i_s, j_s, i_e, j_e = move(i_s, j_s, i_e, j_e, d)
    if not is_moved:
        break
    time += 1
    # print('time, i_s, j_s, i_e, j_e', time, i_s, j_s, i_e, j_e)
    # print('==================')
print(time+1)