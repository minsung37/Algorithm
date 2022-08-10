# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수삼각형
def solution(triangle):
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i + 1])):
            # 삼각형의 시작이거나 끝이거나
            if j == 0 or j == len(triangle[i + 1]):
                triangle[i + 1][j] = triangle[i + 1][j] + triangle[i][j]
            # j가 끝값이 아니면 j - 1 과 j 중 큰값이 더해짐
            else:
                triangle[i + 1][j] = triangle[i + 1][j] + max(triangle[i][j - 1:j + 1])
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))