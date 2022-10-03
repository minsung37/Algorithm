# 약수의 개수와 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    def divisor(n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        if len(result) % 2 == 0:
            return True
        return False

    answer = 0
    for i in range(left, right + 1):
        if divisor(i):
            answer = answer + i
        else:
            answer = answer - i
    return answer


print(solution(13, 17))
print(solution(24, 27))