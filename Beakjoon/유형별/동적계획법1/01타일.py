# 입력값 받기
n = int(input())
# 0 1 2 만드는 경우의수
array = [0,1,2]

# 점화식
for i in range(3, n + 1):
    a = array[i - 1] + array[i - 2]
    array.append(a % 15746)

# 정답출력
print(array[n])
# 15746으로 안나누고 넣으면 메모리초과 나옴
