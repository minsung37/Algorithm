# n : 1 ~ n 까지배열 m : 찾아야하는 수의 개수
n, m = map(int, input().split())
# 찾아야하는 수
target = list(map(int, input().split()))

# n까지 배열 생성
array = []
for i in range(n):
    array.append(i + 1)

# 카운트
count = 0
for j in target:
    # target값이 array[0]가 될떄 까지 반복
    while True:
        if j == array[0]:
            array.pop(0)
            break
        else:
            # target값이 중앙에서 왼쪽에 있다
            # 왼쪽으로 밀어야 최소
            if array.index(j) + 1 <= (len(array) // 2) + 1:
                array.append(array.pop(0))
                count = count + 1
            # target값이 중앙에서 오른쪽에 있다
            # 오른쪽으로 밀어야 최소
            else:
                array.insert(0,array.pop())
                count = count + 1

# 정답 출력
print(count)