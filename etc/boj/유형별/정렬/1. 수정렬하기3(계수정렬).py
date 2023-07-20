import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for i in range(n):
    num = int(input())
    # 입력받은수에 해당 하는 인덱스 값을 증가시킴
    count[num] = count[num] + 1

# 정답 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i)