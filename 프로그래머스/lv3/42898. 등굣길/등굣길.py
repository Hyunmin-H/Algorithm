def print_2d(a):
    for i in a:
        for j in i : 
            print(j, end=' ')
        print()

def solution(m, n, puddles):
    answer = 0
    ans_2d = [[0 for _ in range(m)] for _ in range(n)]
    
    for j, i in puddles:
        ans_2d[i-1][j-1] = -1
    
    is_puddle = False
    for i in range(n):
        if ans_2d[i][0] == -1 : 
            is_puddle = True
        if is_puddle : 
            ans_2d[i][0] = 0
        else : 
            ans_2d[i][0] = 1
    
    is_puddle = False 
    for j in range(m):
        if ans_2d[0][j] == -1 :
            is_puddle = True
        if is_puddle :
            ans_2d[0][j] = 0
        else : 
            ans_2d[0][j] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if ans_2d[i][j] == -1 :
                ans_2d[i][j] = 0
                continue
            ans_2d[i][j] = (ans_2d[i-1][j] + ans_2d[i][j-1]) % 1000000007
                
    
    return ans_2d[n-1][m-1] 