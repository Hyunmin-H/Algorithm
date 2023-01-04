def solution(s):
    answer = ''
    ss = s.split(' ')
    ns = []
    for sss in ss :
        print(sss[1:])
        if sss[0] == '-':
            num = int(sss[1:])*(-1)
        else :
            num = int(sss)
        ns.append(num)

    answer = str(min(ns)) + ' '+ str(max(ns))
    return answer