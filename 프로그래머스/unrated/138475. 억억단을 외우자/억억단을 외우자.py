def solution(e, starts):
    answer = []

    counts = [0] * (e+1)

    for i in range(1, e+1):
        if i*i <= e :
            counts[i*i] += 1
        for j in range(i+1, e+1):
            if i * j > e : 
                break
            counts[i*j] += 2

    max_i = counts.index(max(counts))

    max_list = [0] * (e+1)

    max_value = counts[1]
    max_i = 1
    for i in range(e, 0, -1):
        if counts[i] >= max_value : 
            max_list[i] = i 
            max_value = counts[i]
            max_i = i

        else : 
            max_list[i] = max_i
    for s in starts : 
        answer.append(max_list[s])
    return [max_list[s] for s in starts]