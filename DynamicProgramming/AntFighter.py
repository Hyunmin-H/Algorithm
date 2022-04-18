N = int(input())
a = list(map(int, input().split()))

d = [0] * 100
d[0] = a[0]
d[1] = a[1]
d[3] = a[0] + a[2]
for i in range(3, N):
    d[i] = a[i] + max(d[i-3], d[i-2])

print(max(d[N-1], d[N-2]))
