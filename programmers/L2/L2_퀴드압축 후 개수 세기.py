# 쿼드압축 후 개수 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    answer, n = [0, 0], len(arr)

    def quad(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    k = n // 2
                    quad(x, y, k)
                    quad(x + k, y, k)
                    quad(x, y + k, k)
                    quad(x + k, y + k, k)
                    return
        answer[init] = answer[init] + 1

    quad(0, 0, n)
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
