def solution(s):
    answer = 10000
    for n in range(1, len(s)//2+1):
        result = ''
        num_same = 0
        last = 0
        for i in range(len(s)//n):
            if num_same == 0:
                c = s[i*n:(i+1)*n]
                num_same+=1
            else :
                if c == s[i*n:(i+1)*n]:
                    num_same +=1 
                else :
                    if num_same == 1 :
                        result += c
                    else :
                        result += str(num_same)+c
                    num_same = 1
                    c = s[i*n:(i+1)*n]
            last = i
        if num_same == 1 :
            result += c
        else :
            result += str(num_same) + c
        if last < len(s)-1 :
            result += s[(last+1)*n:]

        answer = min(answer, len(result))

    if len(s) ==1 :
        answer = 1

    return answer