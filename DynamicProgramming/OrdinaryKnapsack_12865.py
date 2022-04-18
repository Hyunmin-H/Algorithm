N, K = map(int, input().split())

W = []
V = []
d = [[0] * (K+1) for _ in range(N)]

 
for _ in range(N):
    x, y = map(int, input().split())
    W.append(x) 
    V.append(y)

for i in range(N):
    for w in range(1, K+1):
        if w < W[i] : 
            d[i][w] = d[i-1][w]
        else : 
            if d[i-1][w-W[i]] + V[i] > d[i-1][w] :
                d[i][w] = d[i-1][w-W[i]] + V[i]
            else :
                d[i][w] = d[i-1][w]

print(d[N-1][K])
















# sum_w = 0
# sum_v = 0
# for i in range(N):
#     sum_w = W[i]
#     sum_v = V[i]
#     for ii in range(i+1, N):
#         if sum_w + W[ii] <= K : 
#             if d[sum_w + W[ii]-1] < sum_v + V[ii]: 
#                 d[sum_w + W[ii]-1] = sum_v + V[ii]
#                 sum_w = sum_w + W[ii]
#                 sum_v = sum_v + V[ii]
#     sum_w = 0
#     sum_v = 0

# print(max(d))



