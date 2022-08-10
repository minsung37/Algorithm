# 약수의 개수와 약수들 입력받기
n = int(input())
array = list(map(int, input().split()))
# 오름차순 정렬
array.sort()
# 정답출력
print(array[0] * array[n - 1])
