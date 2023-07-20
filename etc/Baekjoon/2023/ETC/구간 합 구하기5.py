import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[0] * (n + 1)]
for i in range(n):
    graph.append([0] + list(map(int, input().split())))

# 가로방향 더하기
for i in range(n + 1):
    for j in range(1, n + 1):
        graph[i][j] = graph[i][j] + graph[i][j - 1]

# 세로방향 더하기
for i in range(n + 1):
    for j in range(1, n + 1):
        graph[j][i] = graph[j][i] + graph[j - 1][i]

# 크기 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x1 - 1][y2] - graph[x2][y1 - 1] + graph[x1 - 1][y1 - 1])