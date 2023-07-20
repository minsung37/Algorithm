# 광물 캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927
def solution(picks, minerals):
    answer = int(1e9)

    def backtracking(depth, tired):
        nonlocal answer
        if sum(picks) == 0:
            answer = min(answer, tired)
            return

        for index, pick in enumerate(picks):
            temp = 0
            if pick > 0:
                picks[index] = picks[index] - 1
                if index == 0:
                    for i in range(depth * 5, (depth + 1) * 5):
                        if i >= len(minerals):
                            answer = min(answer, tired + temp)
                            picks[index] = picks[index] + 1
                            return
                        temp = temp + 1
                if index == 1:
                    for i in range(depth * 5, (depth + 1) * 5):
                        if i >= len(minerals):
                            answer = min(answer, tired + temp)
                            picks[index] = picks[index] + 1
                            return
                        if minerals[i] == "diamond":
                            temp = temp + 5
                        else:
                            temp = temp + 1
                if index == 2:
                    for i in range(depth * 5, (depth + 1) * 5):
                        if i >= len(minerals):
                            answer = min(answer, tired + temp)
                            picks[index] = picks[index] + 1
                            return
                        if minerals[i] == "diamond":
                            temp = temp + 25
                        elif minerals[i] == "iron":
                            temp = temp + 5

                        else:
                            temp = temp + 1
                backtracking(depth + 1, tired + temp)
                picks[index] = picks[index] + 1

    backtracking(0, 0)
    return answer


print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))