def solution(cacheSize, cities):
    answer = 0
    
    dict = {}
    time = 0
    if cacheSize == 0 : 
        return len(cities) * 5
    for city in cities : 
        city = city.lower()
        ## 1씩 증가하고 시작
        for d in dict : 
            dict[d] += 1
        ## city가 dict에 있을 경우
            ## 그 value값을 0으로 변경
            ## time을 +1
        if city in dict : 
            dict[city] = 0 
            answer += 1
        else : 
            if len(dict) >= cacheSize : 
                
                max_city = None
                max_num = 0
                for d in dict : 
                    if not max_city :
                        max_city = d
                        max_num = dict[d]
                    if max_num < dict[d]: 
                        max_city = d
                        max_num = dict[d]
                
                del dict[max_city]
                
                dict[city] = 0
            else : 
                dict[city] = 0
            answer +=5
        ## city가 dict에 없을 경우
            ## len(dict)가 캐시 크기보다 크다면
                ## 가장 value값이 큰 key 삭제하고 새로 생성
            ## 그렇지 않다면 새로 생성
        
        
        ## dict의 모든 value값을 +1
    
    return answer