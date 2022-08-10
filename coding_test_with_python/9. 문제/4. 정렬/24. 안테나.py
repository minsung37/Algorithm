# 문제정보 입력받기
n = int(input())
home = list(map(int, input().split()))
home.sort()

# 중간값출력
print(home[(n - 1) // 2])