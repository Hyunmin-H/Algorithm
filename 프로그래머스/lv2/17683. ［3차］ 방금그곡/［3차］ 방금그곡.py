def print_2d(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
        
def solution(m, musicinfos):
    answer = ''
    
    def getLeadTime(start, end):
        h_s, m_s = map(int, start.split(":"))
        h_e, m_e = map(int, end.split(":"))
        
        LT = 0
        if m_s > m_e : 
            LT += 60 - (m_s - m_e)
            LT += (h_e - h_s - 1) * 60
        else : 
            LT += m_e - m_s
            LT += (h_e - h_s) * 60
            
        return LT
    
    def makeMelodyList(m): 
        alpha = ['C', 'D', 'F', 'G', 'A']
        m_list = []
        for i in range(len(m)):
            if i < len(m)-1 and (m[i] in alpha) and m[i+1] =='#':
                m_list.append(m[i]+'#')
            elif m[i] == '#':
                continue
            else :
                m_list.append(m[i])
        return m_list
    
    realMusic_list = []
    
    m_list = makeMelodyList(m)
    for i, musicinfo in enumerate(musicinfos):
        start, end, musicname, melodies = musicinfo.split(',')
        
        melodies_list = makeMelodyList(melodies)
        len_melodies = len(melodies_list)
        leadtime = getLeadTime(start, end)
        
        dp = [[False for _ in range(leadtime)] for _ in range(len(m_list))]
        
        for j in range(len(dp[0])):
            melody = melodies_list[j % len_melodies]
            if m_list[0] == melody :
                dp[0][j] = True

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                melody = melodies_list[j % len_melodies] 
                if m_list[i] == melody and (dp[i-1][j-1]) : 
                    dp[i][j] = True
                    
        for j in range(len(dp[0])):
            if dp[len(m_list)-1][j] :    
                start_time = list(map(int, start.split(":")))
                realMusic_list.append([leadtime, start_time, musicname])
                break
                
    if len(realMusic_list) == 0 : 
        return "(None)"
    else : 
        
        lt, start, mn = max(realMusic_list)
        # start_min = [start, mn]
        for i in range(len(realMusic_list)):
            if realMusic_list[i][0] == lt :
                return realMusic_list[i][2]
                # if realMusic_list[i][1][0] < start_min[0][0] : 
                #     start_min = [realMusic_list[i][1], realMusic_list[i][2]]
                # elif realMusic_list[i][1][0] == start_min[0][0] : 
                #     if realMusic_list[i][1][1] == start_min[0][1] : 
                #         start_min = [realMusic_list[i][1], realMusic_list[i][2]]
                        
        # return start_min[1]
    

## "(None)" 처리 -> 테케 8개?
## 재생 시간도 같을 경우 먼저 입력된 음악 return -> 테케 3개 틀림
## C만 # 처리함 -> 해결 -> 테케 1개 틀림 21 번
