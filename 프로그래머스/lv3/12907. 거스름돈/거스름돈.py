def solution(n, money):
    answer = 0
    
    dp = [0] * (n+1)
    
    for m in money : 
        for i in range(m, n+1):
            if i == m : 
                dp[i] += 1
            else : 
                dp[i] += dp[i-m]
    
    answer = dp[n] % 1000000007
        
    return answer