a = input()

col = a[:1]
row = int(a[1:])

if col =='a': 
    col = 1
elif col =='b':
    col = 2
elif col =='c':
    col = 3
elif col =='d':
    col = 4
elif col =='e':
    col = 5
elif col =='f':
    col = 6
elif col =='g':
    col = 7
elif col =='h':
    col = 8

dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, -1, 1]

cnt = 0
for i in range(8): 
    if 0< row + dy[i] <= 8 and 0< col + dx[i] <= 8 :
        cnt +=1
    
print(cnt)

