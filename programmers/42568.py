# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발
def solution1(progresses, speeds):
    answer, count, time = [], 0, 0
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count = count + 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time = time + 1
    answer.append(count)
    return answer


def solution2(progresses, speeds):
    answer, count = [], 0
    while progresses:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count = count + 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
    answer.append(count)
    return answer