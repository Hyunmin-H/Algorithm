def solution(book_time):
    answer = 0
    times = [0] * (25*60)
    
    for i, (start, end) in enumerate(book_time):
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        
        times[h1*60 + m1] += 1
        times[h2*60 + m2+10] -= 1
    
    for i in range(1, len(times)):
        times[i] += times[i-1]
    
    return max(times)