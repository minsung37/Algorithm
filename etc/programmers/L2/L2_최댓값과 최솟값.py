# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    nums = s.split()
    for idx, num in enumerate(nums):
        nums[idx] = int(num)
    answer = str(min(nums)) + " " + str(max(nums))
    return answer


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))