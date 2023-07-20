# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    x, y = 0, 0
    result = set()
    for direction in dirs:
        if direction == "U" and x < 5:
            result.add(((x, y), (x + 1, y)))
            x = x + 1
        elif direction == "D" and x > -5:
            result.add(((x - 1, y), (x, y)))
            x = x - 1
        elif direction == "R" and y < 5:
            result.add(((x, y), (x, y + 1)))
            y = y + 1
        elif direction == "L" and y > -5:
            result.add(((x, y - 1), (x, y)))
            y = y - 1
    return len(result)


def solution2(dirs):
    x, y = 0, 0
    direction = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    answer = set()
    for d in dirs:
        nx, ny = x + direction[d][0], y + direction[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    return len(answer) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution2("ULURRDLLU"))
print(solution2("LULLLLLLU"))