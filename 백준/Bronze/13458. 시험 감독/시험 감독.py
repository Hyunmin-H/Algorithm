import math
N = int(input())
N_student = list(map(int, input().split()))

A, B = map(int, input().split())

answer = 0

answer += len(N_student)
for i in range(len(N_student)):
    if N_student[i] - A <= 0 :
        continue
    answer += math.ceil((N_student[i] - A) / B)
print(answer)
