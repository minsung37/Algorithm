from collections import deque

# 카드 입력받기
n = int(input())
queue = deque()

# 카드배열 queue에 넣기
for i in range(n):
    queue.append(i + 1)

# 1개 남을때까지 반복
while len(queue) > 1:
    # 왼쪽제거
    queue.popleft()
    # 왼쪽꺼 뒤로 빼기
    queue.append(queue.popleft())

# 정답출력
print(queue.pop())