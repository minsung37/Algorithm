# 과제 진행하기
# https://school.programmers.co.kr/learn/courses/30/lessons/176962
def solution(plans):
    answer, stack = [], []

    for index, plan in enumerate(plans):
        h, m = map(int, plan[1].split(":"))
        time = h * 60 + m
        plan[1] = time
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans) - 1):
        work = plans[i + 1][1] - plans[i][1]
        remain = work - plans[i][2]

        if remain >= 0:
            answer.append(plans[i][0])
            while stack and remain > 0:
                name, time = stack.pop()
                origin_remain = remain
                remain = remain - time
                if remain < 0:
                    stack.append([name, time - origin_remain])
                    break
                answer.append(name)
        else:
            ready = [plans[i][0], plans[i][2] - work]
            stack.append(ready)

    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer


print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
