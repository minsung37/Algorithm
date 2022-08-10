# 반복 횟수 입력받기
t = int(input())
for i in range(t):
    # 위치와 순위정보 입력받기
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    array = []
    for k in range(n):
        array.append(k)
    # 카운트
    count = 0
    while True:
        # 인쇄할곳의 순위가 가장 높으면
        if queue[0] == max(queue):
            a = queue.pop(0)
            b = array.pop(0)
            count = count + 1
            # 인쇄한것이 m 이면
            if b == m:
                break
        else:
            # 위치와 순위 정보를 같이 바꿈
            queue.append(queue.pop(0))
            array.append(array.pop(0))
    # 결과 출력
    print(count)
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1