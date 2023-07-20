from collections import deque
import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]

ground = [[5] * n for _ in range(n)]
trees_queue = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    trees_queue[x - 1][y - 1].append(age)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

for _ in range(k):
    # 봄여름
    for x in range(n):
        for y in range(n):
            tree = trees_queue[x][y]
            tree_state = deque()
            dead_tree = 0
            while tree:
                age = tree.popleft()
                # 양분 충분해서 나이먹은 경우
                if ground[x][y] >= age:
                    ground[x][y] = ground[x][y] - age
                    tree_state.append(age + 1)
                # 나이만큼 양분 못먹음 => 죽은트리에 추가
                else:
                    dead_tree = dead_tree + age // 2
            trees_queue[x][y] = tree_state
            ground[x][y] = ground[x][y] + dead_tree
    # 가을
    new_tree = []
    for x in range(n):
        for y in range(n):
            # 겨울
            ground[x][y] = ground[x][y] + nutrient[x][y]
            for age in trees_queue[x][y]:
                if age % 5 == 0 and age > 0:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            new_tree.append([nx, ny])
    for x, y in new_tree:
        trees_queue[x][y].appendleft(1)
result = 0
for x in range(n):
    for y in range(n):
        result = result + len(trees_queue[x][y])
print(result)