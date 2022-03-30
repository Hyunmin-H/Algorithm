N, M = map(int, input().split())
i, j, d = map(int, input().split())

land = []
direction = d
v = [[0]*M for _ in range(N)]
v[i][j] = 1

for _ in range(N):
    land.append(list(map(int, input().split())))
print(land)

answer = 0 

dx = [0, -1,  0,1]
dy = [-1, 0, 1, 0] #북, 서, 남, 동

count = 1

while True : 

    dont_go = True
    for _ in range(4):
        direction = (direction+1) % 4
        temp_i = i + dy[direction]
        temp_j = j + dx[direction]
        if land[temp_i][temp_j] == 1 or v[temp_i][temp_j] == 1 :
            continue
        else : 
            i = temp_i
            j = temp_j
            dont_go = False
            count +=1
            v[i][j] = 1
        print("i, j, d", i, j, d)

    if dont_go : 
        i = i + dy[(direction+2)%4]
        j = j + dx[(direction+2)%4]
        print("i, j, d", i, j, d)

        if land[i][j] == 1 : 
            print("count:", count)
            break
        count +=1
        v[i][j] = 1
        
        
print(count)

    

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''