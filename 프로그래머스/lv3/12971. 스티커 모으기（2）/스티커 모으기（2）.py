def solution(sticker):
    answer = 0

    dp1 = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]

    if len(sticker) <=3 :
        return max(sticker)

    dp1[0] = sticker[0]
    dp1[2] = dp1[0] + sticker[2]
    dp2[1] = sticker[1]
    dp2[2] = sticker[2]

    for i in range(3, len(sticker)-1):
            dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-3]+sticker[i])

    for i in range(3, len(sticker)):
            dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-3]+sticker[i])
            
    return max(dp1[len(sticker)-2], dp1[len(sticker)-3],dp2[len(sticker)-1], dp2[len(sticker)-2])