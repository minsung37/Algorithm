# [1차] 셔틀버스
# https://school.programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, t, m, timetable):
    start, result = 540, 0
    for index, time in enumerate(timetable):
        h, m_ = map(int, time.split(":"))
        time = h * 60 + m_
        timetable[index] = time
    timetable.sort(reverse=True)

    for order in range(n):
        time = start + t * order
        bus = []
        while timetable and len(bus) < m:
            if timetable[-1] <= time:
                bus.append(timetable.pop())
            else:
                break
        if order == n - 1:
            result = time
            if len(bus) == m:
                result = bus[-1] - 1

    h, m_ = result // 60, result % 60
    answer = []
    if h < 10:
        answer.append("0")
    answer.append(str(h))
    answer.append(":")
    if m_ < 10:
        answer.append("0")
    answer.append(str(m_))
    return "".join(answer)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))