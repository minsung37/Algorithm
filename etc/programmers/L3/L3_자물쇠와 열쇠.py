# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def solution(key, lock):
    n, m = len(key), len(lock)

    def is_open(key):
        for x in range(m):
            for y in range(m):
                if key[x][y] == lock[x][y]:
                    return False
        return True

    def lotate(key):
        lotate_key = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                lotate_key[i][j] = key[n - 1 - j][i]
        return lotate_key

    for _ in range(4):
        for i in range(-m + 1, m):
            for j in range(-m + 1, m):
                new_key = [[0] * m for _ in range(m)]
                for x in range(m):
                    for y in range(m):
                        nx = x + i
                        ny = y + j
                        if 0 <= nx < n and 0 <= ny < n:
                            new_key[x][y] = key[nx][ny]
                if is_open(new_key):
                    return True
        key = lotate(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))