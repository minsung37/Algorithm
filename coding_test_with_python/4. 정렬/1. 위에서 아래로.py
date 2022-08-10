# n을 입력받기
n = int(input())
# n개의 정수를 입력받아 리스트에 저장
a = []
for i in range(n):
    a.append(int(input()))
# 파이썬 기본 라이브러리 사용하여 내림차순 정렬
a.sort(reverse=True)
# 출력
for i in range(n):
    print(a[i], end=' ')

# 3
# 15
# 27
# 12