def solution(strings, n):
    answer = []
    strings = sorted(strings)
    
    answer = sorted(strings, key= lambda a : a[n])
    return answer