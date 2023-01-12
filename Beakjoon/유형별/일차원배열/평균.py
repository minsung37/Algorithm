import sys

n = int(input())
score = list(map(int, sys.stdin.readline().split()))

# 최대값
m = max(score)

for i in range(n):
    new = score[i] * 100 / m
    score[i] = new
# 평균
avg = sum(score)/n

print(avg)