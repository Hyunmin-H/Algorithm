def solution(today, terms, privacies):
    answer = []
    def YMD(d):
        return map(int, d.split("."))
    def addD(D, month):
        y, m, d = YMD(D)
        
        
        if m + month > 12:
            if (m+month) % 12 == 0 :
                y += (m+month)//12 -1
                m = 12
            else :
                y += (m+month)//12
                m = (m+month) % 12
        else : 
            m += month
        return y, m, d
    
    def compareD(D1, D2):
        y1, m1, d1 = D1
        y2, m2, d2 = D2
        
        if y1 < y2 : return True
        elif y1 > y2 : return False 
        
        if m1 < m2 : return True
        elif m1 > m2 : return False
    
        if d1 < d2 : return True
        return False
    
    def isTrash(info_d, info_month, today):
        next_d = addD(info_d, info_month)
        today_d = YMD(today)
        
        return compareD(today_d, next_d)
            
            
    
    infos = {}
    for x in terms: 
        info, month = x.split(" ")
        infos[info] = int(month)
    
    for i, S in enumerate(privacies) : 
        info_d, info = S.split(" ")
        if not isTrash(info_d, infos[info], today) : 
            answer.append(i+1)
    return answer