# [카카오 인턴] 경주로 건설
# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque


def solution(board):
    n = len(board)
    # 0123 - 우좌하상
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(init_direction):
        graph = [[int(1e9)] * n for _ in range(n)]
        graph[0][0] = 0
        queue = deque()
        queue.append((0, 0, 0, init_direction))

        while queue:
            x, y, cost, direction = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                new_dir = i

                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                    continue

                if new_dir == direction:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600

                if new_cost < graph[nx][ny]:
                    graph[nx][ny] = new_cost
                    queue.append((nx, ny, new_cost, i))

        return graph[-1][-1]
    return min(bfs(0), bfs(2))


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))
