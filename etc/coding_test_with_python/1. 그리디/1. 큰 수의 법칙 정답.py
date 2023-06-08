# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째로 큰 수

# 가장 큰수가 더해지는 횟수 계산
count = (m / k + 1) * k
count = count + m % (k + 1)  # 6665 6665 [666] => 대괄호 부분

result = 0
result = result + count * first  # 가장 큰 수 더하기
result = result + (m-count) * second  # 두 번째로 큰 수 더하기

print(result)