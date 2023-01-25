def print_2d(a):
    for i in a:
        for j in i :
            print(j, end=' ')
        print()
        
def solution(users, emoticons):
    answer = []
    def calculate(rates, emoticons, users):
        
        n_plus = 0
        total_price = 0
        
        for rate_user, price_user in users :
            total_price_user = 0
            for i, [rate, emo] in enumerate(zip(rates, emoticons)):
                if rate >=rate_user :
                    price = (1 - rate * 0.01) * emo
                    total_price_user += price
            if total_price_user >= price_user :
                n_plus +=1
            else :
                total_price += total_price_user
        return n_plus, total_price
                

    def backtracking(rates, emoticons, users):
        if len(rates) == len(emoticons):
            n_plus, total_price = calculate(rates, emoticons, users)
            n_pluses.append(n_plus)
            total_prices.append(total_price)
        else : 
            for i in range(10, 41, 10):
                rates.append(i)
                backtracking(rates, emoticons, users)
                rates.pop()
                
    n_pluses = []
    total_prices = []
        
    backtracking([], emoticons, users)
    max_n_plus = max(n_pluses)
    max_price = 0
    for i, [n_plus, total_price] in enumerate(zip(n_pluses, total_prices)) : 
        if n_plus == max_n_plus :
            max_price = max(max_price, total_price)
            
    
        
            

    
    return [max_n_plus, max_price]