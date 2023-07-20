# 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    graph[1][1] = 1

    for y, x in puddles:
        graph[x][y] = 2

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if graph[x][y] == 2:
                graph[x][y] = 0
                continue
            graph[x][y] = graph[x][y] + (graph[x][y - 1] + graph[x - 1][y]) % 1000000007

    return graph[-1][-1]


print(solution(4, 3, [[2, 2]]))