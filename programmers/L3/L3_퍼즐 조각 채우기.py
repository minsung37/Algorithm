# 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
from collections import deque


def solution(game_board, table):
    def bfs(sx, sy):
        nonlocal shape_list
        queue = deque()
        queue.append([sx, sy])
        visited = [[0] * 11 for _ in range(11)]
        xx, yy = 5, 5
        visited[xx][yy] = 1
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if table[nx][ny] == 0:
                    continue
                nxx = xx + dx[d]
                nyy = yy + dy[d]
                queue.append([nx, ny])
                table[nx][ny] = 0
                visited[nxx][nyy] = 1
        shape_list.append(visited)

    def rotate(shape):
        lotate_key = [[0] * 11 for _ in range(11)]
        for i in range(n):
            for j in range(n):
                lotate_key[i][j] = shape[n - 1 - j][i]
        return lotate_key

    answer = -1
    shape_list = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 테이블 모양 담기
    n, m = len(table), len(table[0])
    for x in range(n):
        for y in range(m):
            if table[x][y] == 1:
                bfs(x, y)

    # 순열 + 회전
    nn = len(shape_list)
    permu = [False] * nn

    def permutation(array):
        if len(array) == len(shape_list):
            print(array)
            return
        for i in range(nn):
            if not permu[i]:
                array.append(i)
                permu[i] = True
                permutation(array)
                permu[i] = False
                array.pop()
    permutation([])

    gn, gm = len(game_board), len(game_board[0])



    # return answer


print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
