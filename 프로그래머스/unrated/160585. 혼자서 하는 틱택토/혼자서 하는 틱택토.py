def solution(board):
    answer = -1
    
    ## O와 X의 개수가 2 이상 차이날 경우 fail
    ## 3개 표시가 O, X 모두 있는 경우
    ## 결판나지 않았는데 종료된 경우
    ##      3개 표시가 없을 경우
    ##          그러나 9개 값 모두 채워져있는 경우는 예외
    def has_3samevalue():
        is_O = False
        is_X = False 
        
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] : 
                if board[i][0] == 'O':
                    is_O = True
                elif board[i][0] == 'X':
                    is_X = True
                    
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] : 
                if board[0][j] == 'O':
                    is_O = True
                elif board[0][j] == 'X':
                    is_X = True
        
        if board[0][0] == board[1][1] == board[2][2] : 
            if board[0][0] == 'O':
                is_O = True
            elif board[0][0] == 'X':
                is_X = True
        if board[0][2] == board[1][1] == board[2][0] : 
            if board[0][2] == 'O':
                is_O = True
            elif board[0][2] == 'X':
                is_X = True
            
        return is_O, is_X
    
    num_O = 0
    num_X = 0
    for n in board:
        for m in n:
            if m == 'O' : 
                num_O += 1
            elif m == 'X':
                num_X += 1
                
    if num_O - num_X < 0 or num_O - num_X > 1 : 
        return 0
    
    is_O, is_X = has_3samevalue()
    
    print('is_O', is_O, 'is_X', is_X)
    if is_O and is_X : 
        return 0
    
    if num_O == num_X and is_O :  ## 테케 3개 실패
        return 0
    
    if num_O - num_X == 1 and is_X :  ## 테케 3개 실패
        return 0
    # if not is_O and not is_X :
    #     if num_O + num_X == 9 : 
    #         print('heere')
    #         return 1
    #     else : 
    #         print('hihi')
    #         return 0
                
    return 1
    
    
    return answer