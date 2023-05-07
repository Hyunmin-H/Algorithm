def solution(routes):
    answer = 0
    print(routes)
    routes_sorted = sorted(routes, key=lambda x:x[1])
    print(routes_sorted)
    
    cam_loc = [routes_sorted[0][1]]
    for i, (start, end) in enumerate(routes_sorted[1:]):
        if start <= cam_loc[-1] : 
            continue
        
        cam_loc.append(end)
    answer = len(cam_loc)
    print('cam_loc', cam_loc)
    
    
    # cam_loc_right = [routes_sorted[-1][0]]
#     routes_sorted = routes_sorted[:-1]
#     routes_sorted.reverse()
#     print(routes_sorted)
#     for i, (start, end) in enumerate(routes_sorted):
#         if end >= cam_loc_right[-1] : 
#             continue
        
#         cam_loc_right.append(start)
#     answer = min(answer, len(cam_loc_right))
    
    return answer