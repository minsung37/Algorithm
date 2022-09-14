# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 키패드 누르기
def solution(numbers, hand):
    answer = ''
    right, left = [3, 6, 9], [1, 4, 7]
    recent_right, recent_left = "#", "*"

    def coordinate(number):
        if number == "*":
            temp = [3, 0]
        elif number == 0:
            temp = [3, 1]
        elif number == "#":
            temp = [3, 2]
        else:
            number = number - 1
            temp = [number // 3, number % 3]
        return temp

    def distance(num, now):
        number = coordinate(num)
        finger = coordinate(now)
        return abs(number[0] - finger[0]) + abs(number[1] - finger[1])

    for number in numbers:
        if number in right:
            answer = answer + "R"
            recent_right = number
        elif number in left:
            answer = answer + "L"
            recent_left = number
        else:
            if distance(number, recent_left) < distance(number, recent_right):
                answer = answer + "L"
                recent_left = number
            elif distance(number, recent_left) > distance(number, recent_right):
                answer = answer + "R"
                recent_right = number
            else:
                if hand == "right":
                    answer = answer + "R"
                    recent_right = number
                else:
                    answer = answer + "L"
                    recent_left = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))