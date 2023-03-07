from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visted):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # queue = [start]
    # 현재 노드를 방문 처리
    visted[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # v = queue.pop()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True


# DFS 메서드 정의
def dfs(graph, v, visted):
    # 현재 노드를 방문처리
    visted[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # v = 1일때 2,3,8 순으로
        # False일떄 dfs호출
        if not visted[i]:
            # print(i)
            dfs(graph, i, visted)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
#        0   1          2       3          4       5       6    7          8
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visted_dfs = [False] * 9
visted_bfs = [False] * 9

# DFS/BFS 수행
print("DFS")
dfs(graph, 1, visted_dfs)
print()
print("BFS")
bfs(graph, 1, visted_bfs)