# 회의시간 입력받기
n = int(input())
time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

# 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[0])
# 끝나는 시간을 기준으로 다시 오름차순
time = sorted(time, key=lambda a: a[1])

# 회의의 마지막 시간을 저장할 변수
last = 0
# 회의 개수를 저장할 변수
conut = 0

for i, j in time:
    # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    if i >= last:
        conut += 1
        last = j

print(conut)
