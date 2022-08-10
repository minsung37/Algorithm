import sys
input = sys.stdin.readline

# 2차원 리스트의 맵 정보 입력받기
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
# 단지수를 카운트
count = 0


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    global count
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문처리 & 단지수 구하기
        graph[x][y] = 0
        count = count + 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 탐색
array = []
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        # 단지가 구해진경우
        if dfs(i, j):
            # 현재까지 단지수 array에 저장
            array.append(count)
            # 단지수 초기화
            count = 0
# 정답출력
array.sort()
print(len(array))
for i in range(len(array)):
    print(array[i])
