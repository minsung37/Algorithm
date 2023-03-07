import sys
input = sys.stdin.readline

# 문제정보 입력받기
n = int(input())
x0 = list(map(int, input().split()))

# 중복을 제외하고 정렬
x1 = sorted(list(set(x0)))

# dic 이용 시간복잡도 낮춤 - {-10: 0, -9: 1, 2: 2, 4: 3}
dic = {x1[i]: i for i in range(len(x1))}
for i in x0:
    print(dic[i], end=' ')