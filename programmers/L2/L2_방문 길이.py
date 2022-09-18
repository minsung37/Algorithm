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


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
