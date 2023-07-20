# 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
def solution(places):
    def check_distance(place):
        check_list = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    check_list.append([x, y])

        manhattan_list = []
        for x in range(len(check_list) - 1):
            for y in range(x + 1, len(check_list)):
                manhattan = abs(check_list[x][0] - check_list[y][0]) + abs(check_list[x][1] - check_list[y][1])
                if manhattan == 1:
                    return False
                if manhattan <= 2:
                    if check_list[x][0] == check_list[y][0]:
                        temp = [check_list[x][0], (check_list[x][1] + check_list[y][1]) // 2]
                        manhattan_list.append(temp)
                    elif check_list[x][1] == check_list[y][1]:
                        temp = [(check_list[x][0] + check_list[y][0]) // 2, check_list[x][1]]
                        manhattan_list.append(temp)
                    else:
                        manhattan_list.append([check_list[x][0], check_list[y][1]])
                        manhattan_list.append([check_list[y][0], check_list[x][1]])

        for x, y in manhattan_list:
            if place[x][y] != "X":
                return False
        return True

    result = []
    for place in places:
        if check_distance(place):
            result.append(1)
        else:
            result.append(0)
    return result


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))