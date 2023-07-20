from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

# 문제조건 입력 받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 정렬하고 중복조합 구하rl => 중복제거 => 정렬
array.sort()
data = list(set(combinations_with_replacement(array, m)))
data.sort()

# 정답 출력
for i in data:
    print(' '.join(map(str, i)))