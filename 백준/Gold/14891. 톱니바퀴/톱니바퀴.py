
from collections import deque

def rotate_one(i, dir):
    if dir == 1 :
        temp = topni[i].pop()
        topni[i].appendleft(temp)
    elif dir == -1 :
        temp = topni[i].popleft()
        topni[i].append(temp)

def rotate(start, dir):

    dirs = [0, 0, 0, 0]
    dirs[start] = dir

    i = start
    while i < 3 :
        if topni[i][2] != topni[i+1][6] :
            dirs[i+1] = -dirs[i]
        i+=1
    i = start
    while i > 0 :
        if topni[i][6] != topni[i-1][2] :
            dirs[i-1] = -dirs[i]
        i-=1
    for i, dir in enumerate(dirs) :
        rotate_one(i, dir)

def calc_score():
    score = 0
    if topni[0][0] == 1 :
        score += 1
    if topni[1][0] == 1 :
        score += 2
    if topni[2][0] == 1 :
        score += 4
    if topni[3][0] == 1 :
        score += 8
    return score


topni = []
for _ in range(4):
    topni.append(deque(map(int, input())))

K = int(input())
for k in range(K) :
    start, dir = map(int, input().split())
    rotate(start-1, dir)
print(calc_score())