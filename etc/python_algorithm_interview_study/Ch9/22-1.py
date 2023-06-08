# https://leetcode.com/problems/daily-temperatures/
# 1518ms 25MB
class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        answer, stack = [0] * len(temperatures), []
        for index, temperature in enumerate(temperatures):
            while stack:
                # 따뜻한 날인경우
                if temperature > temperatures[stack[-1]]:
                    # 스택에서 빼서
                    last = stack.pop()
                    # 날짜의 차이를 구한다.
                    answer[last] = index - last
                else:
                    break
            stack.append(index)
        return answer


print(Solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1,1,4,2,1,1,0,0]
