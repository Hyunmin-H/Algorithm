
class Status: 
    def __init__(self, *args):
        if len(args)<2:
            self.shark_num = 0
            self.shark_dir = 0
            self.smell_sharknum = 0
            self.smell_time = 0
        else:
            self.shark_num = args[0]
            self.shark_dir = args[1]
            self.smell_sharknum = args[0]
            self.smell_time = k

def SharkMove(Shark_loc, Statuses):
    # 상어마다 이동 숫자가 작은 상어부터 이동
    for n in range(M):
        cur_dir = Statuses[Shark_loc[n][0]][Shark_loc[n][1]].shark_dir
        cur_i = Shark_loc[n][0]
        cur_j = Shark_loc[n][1]
        for i in range(4): # 4가지 방향 확인
            temp_dir = dir_priorities[n][cur_dir-1][i] 
            temp_i = cur_i + dy[temp_dir-1]
            temp_j = cur_j + dx[temp_dir-1]
            if temp_i <0 or temp_j <0 or temp_i >=N or temp_j >=N or Statuses[temp_i][temp_j].shark_num >0:
                continue

            elif ddd: 
                pass

            else : # 이동
                Statuses[temp_i][temp_j].shark_num = n+1
                Statuses[temp_i][temp_j].smell_time = k+1
    
                Statuses[Shark_loc[n][0]][Shark_loc[n][1]].shark_num = 0
                Statuses[Shark_loc[n][0]][Shark_loc[n][1]].shark_dir = 0

N, M, k = map(int, input().split())

Shark_location = []

for _ in range(N):
    Shark_location.append(list(map(int, input().split())))

d = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dir_priorities = []

for _ in range(M):
    dir_priority = []
    for _ in range(4):
        dir_priority.append(list(map(int, input().split())))
    dir_priorities.append(dir_priority)

print("dir_prioirity",dir_priorities )
Statuses = []
Shark_loc = [[0, 0]] * M ## 상어 숫자 별로 위치 index 저장
for i in range(N):
    temp = []
    for j in range(N):
        if Shark_location[i][j] > 0:
            temp.append(Status(Shark_location[i][j], d[Shark_location[i][j]-1]))
            # print('Shark_location[i][j]-1', Shark_location[i][j]-1)
            # print('Shark_loc', Shark_loc)
            Shark_loc[Shark_location[i][j]-1] = [i, j]
        else : 
            temp.append(Status())

    Statuses.append(temp)
answer = 0

while answer <1000:

    SharkMove(Shark_loc, Statuses)

    #이동한다.
        # 상어를 만나면 쫓아낸다.
    

    #향수 뿌린다.





    answer+=1



answer = -1
print("answer :", answer)
