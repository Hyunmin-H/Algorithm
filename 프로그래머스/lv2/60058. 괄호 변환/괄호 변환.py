def solution(p):
    answer = ''
    
    def divide_two(w):
        n1 = 0 ## ( 개수
        n2 = 0 ## ) 개수
        
        u = ''
        v = ''
        
        for i in range(len(w)) :
            if w[i] == '(':
                n1 += 1
            elif w[i] == ')' : 
                n2 += 1 
                
            if n1 == n2 :
                u = w[:i+1]
                v = w[i+1:]
                break
        return u, v
    
    def is_rightString(s):
        n1 = 0
        n2 = 0
        for i in range(len(s)):
            if s[i] == '(':
                n1 += 1
            else :
                n2 += 1
            if n2 > n1 : 
                return False
        return True
    def func(s):
        t =''
        for i in range(1, len(s)-1):
            if s[i] =='(':
                t += ')'
            else :
                t += '('
        return t
    
    def make_rightString(w):
        if len(w) == 0 :
            return w
        
        u, v = divide_two(w)
        print(u, v)
        
        if is_rightString(u):
            return u + make_rightString(v)
        else :
            return '(' + make_rightString(v) + ')' + func(u)
            
        
    print(make_rightString(p))
        
    return make_rightString(p)