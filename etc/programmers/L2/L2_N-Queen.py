# N-Queen
# https://school.programmers.co.kr/learn/courses/30/lessons/12952
def solution(n):
    def queen(chess, n, x):
        count = 0
        if n == x:
            return 1
        for y in range(n):
            chess[x] = y
            for k in range(x):
                if chess[k] == chess[x]:
                    break
                if abs(chess[k] - chess[x]) == abs(x - k):
                    break
            else:
                count = count + queen(chess, n, x + 1)
        return count
    chess = [0] * n
    return queen(chess, n, 0)


print(solution(4))
print(solution(5))