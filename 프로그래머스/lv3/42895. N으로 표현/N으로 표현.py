def solution(N, number):
    answer = 0 
    set_list = [{N}]
    if number == N:
        return 1
    for cnt in range(2, 9):
        s = set()
        temp=''
        for i in range(cnt):
            temp+=str(N)
        s.add(int(temp))
        for cnt_ in range(1, cnt):
            for a in set_list[cnt_-1]:
                for b in set_list[cnt-cnt_-1]:
                    
                    s.add(a+b)
                    s.add(a*b)
                    if a-b >0 :
                        s.add(a-b)
                    if b != 0 and a//b > 0 :
                        s.add(a//b)
        if number in s:
            return cnt
        set_list.append(s)
    
    
    return -1