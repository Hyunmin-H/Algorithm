def print_2d(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
        
def solution(board, skill):
    answer = 0
    
    H = len(board)
    W = len(board[0])
    
    sum_board = [[0 for _ in range(W+1)] for _ in range(H+1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1 : 
            degree *= -1
        
        sum_board[r1][c1] += degree
        sum_board[r2+1][c2+1] += degree
        sum_board[r1][c2+1] -= degree
        sum_board[r2+1][c1] -= degree
    
    for j in range(1, W):
        for i in range(H):
            sum_board[i][j] += sum_board[i][j-1]
    
    for i in range(1, H):
        for j in range(W):
            sum_board[i][j] += sum_board[i-1][j]
    
    for i in range(H):
        for j in range(W):
            s = board[i][j] + sum_board[i][j]
            if s > 0 :
                answer += 1
    
    
    
    
    return answer