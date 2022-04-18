N = int(input())

a = []
d = [0] * N
for i in range(N):
    a.append(list(map(int, input().split())))


for i in range(N):
    if i + a[i][0] - 1 > N-1 :
        continue
    else : 
        if i == 0 : 
            d[i + a[i][0] - 1] = a[i][1] 
        else : 
            d[i + a[i][0] - 1] = max(d[i + a[i][0] - 1],  a[i][1] + max(d[:i]))

print(max(d))



