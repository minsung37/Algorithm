from collections import Counter

# 반복횟수
t = int(input())

# 입력받아서 옷의 종류만 리스트에 넣기
for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)
    # 같은분류 몇개인지 세기
    wear_Counter = Counter(wear)
    # 각 종류마다 항목의 개수
    cnt = 1
    for key in wear_Counter:
        cnt = cnt * (wear_Counter[key] + 1)
    # 정답 출력
    print(cnt-1)

# 모자3 바지1 상의1 => 4*2*2-1