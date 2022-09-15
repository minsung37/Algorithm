# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기
def solution(numbers):
    result = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    answer = sorted(list(result))
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
