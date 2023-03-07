from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

# 문제조건 입력 받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 정렬하고 중복조합 구하기
array.sort()
data = list(combinations_with_replacement(array, m))

# 정답 출력
for i in data:
    print(' '.join(map(str, i)))