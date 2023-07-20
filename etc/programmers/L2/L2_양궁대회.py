# 양궁대회
# https://school.programmers.co.kr/learn/courses/30/lessons/92342
def solution(n, info):
    answer, temp, max_diff = [0] * 11, [0] * 11, 0

    for subset in range(1, 1 << 10):
        ryan, apeach, cnt = 0, 0, 0

        for i in range(10):
            # i번째 원소 존재하는 경우 => 라이언이 이겨야함
            if subset & (1 << i):
                ryan = ryan + (10 - i)
                temp[i] = info[i] + 1
                cnt = cnt + temp[i]
            # i번째 원소 존재하지 않는 경우 => 어피치가 점수 있으면 이김
            else:
                temp[i] = 0
                if info[i]:
                    apeach = apeach + (10 - i)

        if cnt > n:
            continue

        temp[10] = n - cnt
        if ryan - apeach == max_diff:
            for i in reversed(range(11)):
                if temp[i] > answer[i]:
                    max_diff = ryan - apeach
                    answer = temp[:]
                    break
                elif temp[i] < answer[i]:
                    break

        elif ryan - apeach > max_diff:
            max_diff = ryan - apeach
            answer = temp[:]

    if max_diff == 0:
        answer = [-1]

    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))