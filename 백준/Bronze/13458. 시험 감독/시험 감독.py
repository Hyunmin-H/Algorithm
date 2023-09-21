N = int(input())
classes = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for a_i in classes:
    res = a_i - B
    cnt += 1
    if res <= 0:
        continue
    n, r = divmod(res, C)
    cnt += n
    if r != 0:
        cnt += 1

print(cnt)
