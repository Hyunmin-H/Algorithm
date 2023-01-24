def print_2d(a):
    for i in a:
        for j in i:
            print(j, end= ' ')
        print()
        
def solution(places):
    answer = []
    
    dy1 = [-1, 0, 1, 0]
    dx1 = [0, 1, 0, -1]
    
    dy2 = [-1, 1, 1, -1, -2, 0, 2, 0] ## 대각선
    dx2 = [1, 1, -1, -1, 0, 2, 0, -2]
    
    dxdy_idx = [[0, 1], [1, 2], [2, 3], [3, 0], [0], [1], [2], [3]]
    
    def is_protected(place, i, j):
        for n in range(4):
            ii = i + dy1[n]
            jj = j + dx1[n]
            
            if ii < 0 or jj < 0 or ii >= 5 or jj >= 5:
                continue
            if place[ii][jj] == 'P' :
                return False
        for n in range(8):
            ii = i + dy2[n]
            jj = j + dx2[n]
            
            if ii < 0 or jj < 0 or ii >= 5 or jj >= 5:
                continue
            if place[ii][jj] == 'P' :
                for idx in dxdy_idx[n] :
                    iii = i + dy1[idx]
                    jjj = j + dx1[idx]
                    if iii < 0 or jjj < 0 or iii >= 5 or jjj >= 5:
                        continue
                    if place[iii][jjj] == 'O' or place[iii][jjj] == 'P':
                        return False
        return True
            
    
    
    for place in places :
        is_break = False
        
        print_2d(place)
        is_protect = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not is_protected(place, i, j) : 
                        is_protect = False
                        is_break = True
                        break
            if is_break: 
                break
        if is_protect : 
            answer.append(1)
        else :
            answer.append(0)
        print_2d(place)
    
        print("==============")
    return answer