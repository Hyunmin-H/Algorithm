N = int(input())
a = [int(input()) for _ in range(N)] 

def binary_search_and_sort(a_sorted, k):
    q_l = 0
    q_r = len(a_sorted)-1

    while q_l < q_r: 
        if a_sorted[q_l] <= k :



for i in range(N):
    a_sorted = sorted(a[:i+1])
    if i % 2 == 0: # 가운데 숫자 한개
        print(a_sorted[i//2])
    else : 
        print(min(a_sorted[i//2], a_sorted[i//2+1]))
    # print('middle:', a_sorted.middle())
