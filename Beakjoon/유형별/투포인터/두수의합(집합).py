# 수의개수 입력받기
n = int(input())
array = list(map(int, input().split()))
target = int(input())

# 비교할 목표값에서 입력받은수를 빼기
array_comp = [0] * n
for i in range(n):
    array_comp[i] = target - array[i]

# 교집합 개수구하기
array = set(array)
array_comp = set(array_comp)
k = array & array_comp
# array = {1, 2, 3, 5, 7, 9, 10, 11, 12}
# array = {1, 2, 3, 4, 6, 8, 10, 11, 12}
# 더해서 13을 만들수 있으면 짝이 이루어 질것이다.

# 정답출력
print(len(k) // 2)