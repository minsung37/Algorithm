from itertools import permutations
import sys
input = sys.stdin.readline

# 문제조건 입력 받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 순열 구하기 => set으로 중복제거하고 => 정렬
data = list(set(permutations(array, m)))
data.sort()

# 정답 출력
for i in data:
    print(' '.join(map(str, i)))