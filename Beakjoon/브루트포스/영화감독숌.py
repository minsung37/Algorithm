# n번째 영화 제목 찾기
n = int(input())
# 첫번째 영화 제목
title = 666
# n번째 영화 제목을 담을 변수
result = ""

# 제목찾기
while n > 0:
    # "666"이 제목에 있는경우
    if "666" in str(title):
        result = title
        n = n - 1
    title = title + 1

# 정답출력
print(result)