
def print_2darray(graph):

    for i in graph :
        for j in i:
            print(j, end=' ')
        print()


def FishMove(status):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for n in range(1, 17):

        ii = 5
        jj = 5
        ## 물고기가 있는지 탐색
        for i in range(4):
            for j in range(4):
                if status[i][j][0] == n:
                    ii = i 
                    jj = j
        if ii == 5 : # 물고기가 없을 경우 
            continue

        ##물고기가 있는 경우 
        d = status[ii][jj][1]
        for _ in range(8):
            temp_i = ii + dy[d]
            temp_j = jj + dx[d]


            if (temp_i < 0 or temp_j < 0 or temp_i >=4 or temp_j >= 4) or status[temp_i][temp_j][0] == 17 : 
                # 이동 못할 경우
                d = (d+1) % 8
                # status[ii][jj][1] = d
                continue
            else : #switch
                status[ii][jj][1] = d
                temp = status[ii][jj]
                status[ii][jj] = status[temp_i][temp_j]
                status[temp_i][temp_j] = temp
                break

    return status
            
def Search_eatfishes(status, cnt_totalEat):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    #find Shark
    ii = 5
    jj = 5
    for i in range(4):
        for j in range(4):
            if status[i][j][0] == 17:
                ii = i 
                jj = j

    d = status[ii][jj][1]
    temp_i = ii
    temp_j = jj
    
    eatFishes_arr = []
    for _ in range(4):

        temp_i = temp_i + dy[d]
        temp_j = temp_j + dx[d]
        
        if (temp_i < 0 or temp_j < 0 or temp_i >=4 or temp_j >= 4) or status[temp_i][temp_j][0] == 0: 
            continue

        # 잡아먹을 물고기가 있을 경우
        import copy
        eatFishes_arr.append([temp_i, temp_j, copy.deepcopy(status), cnt_totalEat])

    if len(eatFishes_arr) > 0 :
        return eatFishes_arr
    else : 
        return None

status = []
temp = []
for i in range(4):
    temp.append(list(map(int, input().split())))

for i in range(4):
    a = []
    for j in range(4):
        a.append([temp[i][j*2], temp[i][j*2+1]-1])
    status.append(a)

cnt_totalEat = status[0][0][0]
status[0][0][0] = 17

status = FishMove(status)
stack = Search_eatfishes(status, cnt_totalEat)

answer = 0
        
while stack: 
    eatfish = stack.pop()
    temp_status = eatfish[2]

    #find Shark
    ii = 5
    jj = 5
    for i in range(4):
        for j in range(4):
            if temp_status[i][j][0] == 17:
                ii = i 
                jj = j
    # Eat
    cnt_totalEat = eatfish[3] + temp_status[eatfish[0]][eatfish[1]][0]
    temp_status[eatfish[0]][eatfish[1]][0] = 17
    temp_status[ii][jj][0] = 0
    
    temp_status = FishMove(temp_status)

    eatfishes_temp = Search_eatfishes(temp_status, cnt_totalEat)
    if eatfishes_temp is None : 
        answer = max(answer, cnt_totalEat)
    else : 
        stack.extend(eatfishes_temp)

print(answer)
