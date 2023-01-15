import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
blocks = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (1, 0), (0, 1), (1, 1)],
          [(0, 0), (1, 0), (2, 0), (2, 1)],
          [(0, 1), (1, 1), (2, 1), (2, 0)],
          [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (0, 1), (1, 0), (2, 0)],
          [(0, 0), (1, 0), (1, 1), (1, 2)],
          [(0, 2), (1, 1), (1, 2), (1, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)],
          [(0, 0), (1, 0), (0, 1), (0, 2)],
          [(0, 0), (1, 0), (1, 1), (2, 1)],
          [(0, 1), (1, 1), (1, 0), (2, 0)],
          [(1, 0), (1, 1), (0, 1), (0, 2)],
          [(0, 0), (0, 1), (1, 1), (1, 2)],
          [(0, 1), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (1, 0), (1, 1), (2, 0)],
          [(0, 1), (1, 1), (1, 0), (2, 1)]]
size_list = []
for i in range(n):
    for j in range(m):
        for block in blocks:
            size = 0
            for x, y in block:
                nx = i + x
                ny = j + y
                if nx < n and ny < m:
                    size = size + graph[nx][ny]
                else:
                    break
                size_list.append(size)
print(max(size_list))