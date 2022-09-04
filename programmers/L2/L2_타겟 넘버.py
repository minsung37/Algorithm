# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버
def solution(numbers, target):
    answer, n = 0, len(numbers)

    def dfs(target_num, add, sub, count):
        nonlocal answer
        if count == n:
            if target_num == target:
                answer = answer + 1
                return
        if add:
            dfs(target_num + numbers[count], add - 1, sub, count + 1)
        if sub:
            dfs(target_num - numbers[count], add, sub - 1, count + 1)
    for i in range(n):
        dfs(0, i, n - i, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))