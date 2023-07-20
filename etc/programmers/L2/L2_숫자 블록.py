# 숫자 블록
# https://school.programmers.co.kr/learn/courses/30/lessons/12923
def solution(begin, end):
    answer = []
    for number in range(begin, end + 1):
        for div in range(2, int(number ** 0.5) + 1):
            if number % div == 0 and number // div <= 10000000:
                answer.append(number // div)
                break
        else:
            if number == 1:
                answer.append(0)
            else:
                answer.append(1)
    return answer


print(solution(1, 10))