import sys

def print_2d(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
    print('===')
def eat_fish(area, i1, j1, i2, j2):
    area[i1][j1] = [0, 0]
    num_fish = area[i2][j2][0]
    area[i2][j2][0] = -1
    return num_fish, area

def move_fishes(area):
    for n in range(1, 17):
        is_break = False
        for i in range(4):
            for j in range(4):
                if area[i][j][0] == n :
                    d = area[i][j][1]
                    for dd in range(8):
                        ddd = (d + dd) % 8
                        ii = i + dy[ddd]
                        jj = j + dx[ddd]

                        if ii < 0 or jj < 0 or ii >=4 or jj >=4 or area[ii][jj][0] == -1:
                            continue

                        if area[ii][jj][0] >= 0 :
                            area[i][j][1] = ddd
                            temp = area[ii][jj][:]
                            area[ii][jj] = area[i][j][:]
                            area[i][j] = temp[:]
                            is_break = True
                            break
                if is_break :
                    break
            if is_break :
                break
    return area

def is_exist_fish():
    for i in range(4):
        for j in range(4):
            if area[i][j][0] > 0 :
                return True
    return False

def get_shark_ijs(area):
    s_i, s_j = [-1, -1]
    for i in range(4):
        for j in range(4):
            if area[i][j][0] == -1 :
                s_i, s_j = (i, j)

    d = area[s_i][s_j][1]
    shark_ijs = []
    for n in range(1, 5):
        ii = s_i + dy[d] * n
        jj = s_j + dx[d] * n
        if ii < 0 or jj < 0 or ii >=4 or jj>=4 :
            break
        if area[ii][jj][0] == 0 :
            continue
        shark_ijs.append([ii,jj])
    return shark_ijs

def backtracking(area, sum, shark_ij_now):
    area = move_fishes(area)
    shark_ijs = get_shark_ijs(area)

    if len(shark_ijs)==0 :
        global answer
        answer = max(answer, sum)
        return

    for shark_ij in shark_ijs :
        i, j = shark_ij
        import copy
        area_ = copy.deepcopy(area)
        num_fish, area_ = eat_fish(area_, shark_ij_now[0], shark_ij_now[1], i, j)

        backtracking(area_, sum+num_fish, [i, j])

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

# 여러개의 테스트 케이스가 주어지므로, 각각을 
answer = 0
inputs= [list(map(int, input().split())) for _ in range(4)]
area = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        area[i][j] = [inputs[i][j*2], inputs[i][j*2+1]-1]

        ## 상어 첫 자리
answer += area[0][0][0]
area[0][0][0] = -1

backtracking(area, answer, [0, 0])
print(answer)

