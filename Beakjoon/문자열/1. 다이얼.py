# 문제정보 입력받기
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()

# 시간
time = 0
for i in a:
    for j in dial:
        # 문자가 다이얼 안에 있으면
        if i in j:
            # 시간을 더함
            time = time + dial.index(j) + 3

# 정답 출력
print(time)