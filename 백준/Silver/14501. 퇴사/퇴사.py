N = int(input())
T = []
P = []
sum_p = [0] * (N+1)

def print_list(a):
    for i in a :
        print(i, end='\t')
    print()

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

if T[0] <= N :
    sum_p[T[0]] = P[0]
for i in range(1, N):
    if i + T[i] > N :
        continue
    sum_p[i + T[i]] = max(sum_p[i + T[i]], P[i] + max(sum_p[:i+1]))
print(max(sum_p))

