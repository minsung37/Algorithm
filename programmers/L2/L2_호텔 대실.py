# https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 호텔 대실
def solution(book_time):
    for index, time in enumerate(book_time):
        book_time[index] = convert(time)
    result = 0
    stack = []
    book_time.sort()
    for time in book_time:
        if not stack:
            stack.append(time)
            result = max(result, len(stack))
        else:
            new_stack = []
            for info in stack:
                # 이용중인 곳만 스택에 담는다.
                if info[1] > time[0]:
                    new_stack.append(info)
            new_stack.append(time)
            stack = new_stack
            result = max(result, len(stack))
    return result


# 시간 변환 마지막 시간 + 10
def convert(time):
    return [int(time[0][0:2]) * 60 + int(time[0][3:]), int(time[1][0:2]) * 60 + int(time[1][3:]) + 10]


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))