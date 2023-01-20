def solution(survey, choices):
    answer = ''
    score = {'R':0, 'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
    
    def updateScore(q, c):
        if 1<=c<4 :
            score[q[0]] += 4-c
        else : 
            score[q[1]] += c-4
    
    def calcTotalScore(answer):
        if score['R'] >= score['T'] :
            answer += 'R'
        else :
            answer += 'T'
        if score['C'] >= score['F'] :
            answer += 'C'
        else :
            answer += 'F'
        if score['J'] >= score['M'] :
            answer += 'J'
        else :
            answer += 'M'
        if score['A'] >= score['N'] :
            answer += 'A'
        else :
            answer += 'N'
        return answer
        
        
    
    for _, (q, c) in enumerate(zip(survey, choices)):
        updateScore(q, c)
    answer = calcTotalScore(answer)
    print('answer', answer)
    
        
    return answer