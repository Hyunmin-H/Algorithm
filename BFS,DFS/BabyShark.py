from collections import deque


def print_2darray(graph):

    for i in graph :
        for j in i:
            print(j, end=' ')
        print()

N = int(input())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

i_baby = 0
j_baby = 0
size_baby = 2
cnt_eat = 0
time = 0

for i in range(N):
    for j in range(N):
        if area[i][j] == 9 :
            i_baby = i
            j_baby = j


def BFS(i, j, area, cnt_eat, size_baby, time):
    ## 먹이를 1마리 먹을때까지의 BFS 
    q = deque()
    q.append([i, j])
    area[i][j] = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    dist = [[0] * N for _ in range(N)]

    eat_list = []
    eat_dist = 0

    while q:
        ii, jj = q.popleft()
        # print(q)
        # print("dist:")
        # print_2darray(dist)
        
        # print("area:")
        # print_2darray(area)

        if 0 < eat_dist < dist[ii][jj] + 1 : 
            break

        for n in range(4):
            i_temp = ii + di[n]
            j_temp = jj + dj[n]

            if i_temp < 0 or j_temp < 0 or i_temp >=N or j_temp >=N : 
                continue
            
            if 0 < area[i_temp][j_temp] < size_baby : # eat
                eat_list.append([i_temp, j_temp])
                eat_dist = dist[ii][jj] + 1

            elif dist[i_temp][j_temp] == 0 and (area[i_temp][j_temp] == 0 or area[i_temp][j_temp] == size_baby) : # 지나감
                q.append([i_temp, j_temp])
                dist[i_temp][j_temp] = dist[ii][jj] + 1
         
            # else : ## 못지나갈 때 
    if len(eat_list) > 0 :
        best_list = []
        min_i = N
        min_j = N
        best_n = N
        for n in range(len(eat_list)): ## 상
            if min_i > eat_list[n][0] : 
                min_i = eat_list[n][0]
                best_list = []
                best_list.append(n)
            elif min_i == eat_list[n][0] : 
                best_list.append(n)

        for n in best_list : ## 좌 
            if min_j > eat_list[n][1] : 
                min_j = eat_list[n][1]
                best_n = n

        cnt_eat +=1 
        if cnt_eat >= size_baby : # 진화 
            size_baby+=1
            cnt_eat = 0
        time += eat_dist 
        return eat_list[best_n][0], eat_list[best_n][1], cnt_eat, size_baby, time

    else : 
        return None, None, None, None, time
            
while True: 
    i_baby, j_baby, cnt_eat, size_baby, time = BFS(i_baby, j_baby, area, cnt_eat, size_baby, time)
    # print("cnt_eat, size_baby, time :", cnt_eat, size_baby, time)
    if i_baby is None : 
        break

print(time)  

