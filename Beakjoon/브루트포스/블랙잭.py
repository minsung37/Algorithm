# 조합사용
from itertools import combinations
n, m = map(int, input().split())
array = list(map(int, input().split()))

# result C 3 (조합)
result = list(combinations(array,3))
x = len(result)

# 조합갑의 합을 집합에 넣음(중복제거)
score = set()
for i in range(x):
    if sum(result[i]) <= m:
        score.add(sum(result[i])-m)

# 내림차순해서 m과의 차이가 가장 적은 것을 고름
score = list(score)
score.sort(reverse=True)
print(score[0] + m)
