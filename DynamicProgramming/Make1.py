a = int(input())

d = [0] * 30000

for i in range(2, a+1) : 
    d[i] = d[i-1] +1
    if i % 5 == 0 :
        d[i] = min(d[i],d[i//5]+1 ) 
    if i % 3 == 0 :
        d[i] = min(d[i],d[i//3]+1 )  
    if i % 2 == 0 :
        d[i] = min(d[i],d[i//2]+1 ) 
    


print(d[a])







# aa = a
# answer = 0
# while aa > 1 :
#     if aa % 5 == 0 :
#         aa /= 5
#     elif aa % 3 == 0 :
#         aa /= 3
#     elif aa % 2 == 0 :
#         aa /= 2
#     else : 
#         aa -= 1
#     print("aa:", aa)
#     answer +=1

# print(answer)
