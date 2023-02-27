from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    concert = list(map(int, input().split()))
    visited = [False] * (n + 1)

    # BFS
    queue = deque()
    queue.append(home)
    is_arrive = False
    while queue:
        x, y = queue.popleft()
        # 콘서트장 도착가능
        if abs(x - concert[0]) + abs(y - concert[1]) <= 1000:
            is_arrive = True
            break
        # 편의점 갈수 있으면 가기
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = True
    if is_arrive:
        print("happy")
    else:
        print("sad")