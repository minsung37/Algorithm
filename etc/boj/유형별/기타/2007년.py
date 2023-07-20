# 1월 1일 MON
x, y = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# 월을 빼주고 월에 해당하는 일수를 y에 더하기
for i in range(x):
    x = x - 1
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        y = y + 31
    if x == 4 or x == 6 or x == 9 or x == 11:
        y = y + 30
    if x == 2:
        y = y + 28

# 정답출력
print(day[y % 7])