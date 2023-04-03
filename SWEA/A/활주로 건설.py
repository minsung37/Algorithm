import sys
input = sys.stdin.readline


def sol(array):
    # 높이가 모두 평탄한 경우
    if max(array) - min(array) == 0:
        return 1
    # 인접한곳 높이차 1보다 큰경우 불가능
    for i in range(n - 1):
        if abs(array[i] - array[i + 1]) > 1:
            return 0
    # 그 외 경우
    install = [False] * n
    for i in range(n - 1):
        if array[i] != array[i + 1]:
            down, up = i + 1, i
            # 내리막인 경우 오른쪽 탐색
            if array[i] > array[i + 1]:
                for k in range(l):
                    # 길이미달, 이미설치된 경우, 평탄하지 않은경우
                    if down + k >= n or install[down + k] or array[down] != array[down + k]:
                        return 0
                    # 경사로 설치
                    if array[down] == array[down + k]:
                        install[down + k] = True
            # 오르막인 경우 왼쪽 탐색
            else:
                for k in range(l):
                    if up - k < 0 or install[up - k] or array[up] != array[up - k]:
                        return 0
                    if array[up] == array[up - k]:
                        install[up - k] = True
    return 1


T = int(input())
for t in range(T):
    n, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for row in graph:
        result = result + sol(row)
    for x in range(n):
        col = []
        for y in range(n):
            col.append(graph[y][x])
        result = result + sol(col)
    print("#%d %d" % (t + 1, result))