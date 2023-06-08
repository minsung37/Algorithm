n = int(input())
score = []

# 데이터타입 바꿔서 배열에 넣기
for i in range(n):
    [name, kor, eng, math] = map(str, input().split())
    score.append([name, int(kor), int(eng), int(math)])

# 국어(내림차순) 영어(오름차순) 수학(내림차순) 이름(사전순으로 증가)
score = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 정답 출력
for student in score:
    print(student[0])
