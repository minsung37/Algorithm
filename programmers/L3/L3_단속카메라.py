# 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera, spot = 1, routes[0][-1]
    for i in range(1, len(routes)):
        if not (routes[i][0] <= spot and routes[i][1] >= spot):
            camera = camera + 1
            spot = routes[i][1]
    return camera


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))