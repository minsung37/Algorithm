n = int(input())

# 좌표 순서바꿔서 입력받기
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

# 정렬
array.sort()

# 정답출력
for y, x in array:
    print(x, y)