from collections import deque

# 문제조건 입력받기
n, m = map(int, input().split())

# 숨바꼭질 초기공간설정
mx = 100000
array = [0] * (mx + 1)

# BFS 진행
queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    # 찾은경우
    if x == m:
        print(array[x])
        break
    for i in (x - 1, x + 1, x * 2):
        # 다음위치로 갈수 있고 방문한적이 없는경우 => 이미 방문한 적이 있다면 그것은 최단시간이 아니다.
        if 0 <= i <= mx and array[i] == 0:
            array[i] = array[x] + 1
            queue.append(i)
