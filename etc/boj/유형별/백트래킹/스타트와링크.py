import sys
import itertools
input = sys.stdin.readline

# 인원수와 능력치 입력받기
n = int(input())
array = []
team = []
for i in range(n):
    array.append(list(map(int,input().split())))
    team.append(i)

# 팀을 집합으로 변경
team = set(team)
# n//2명의 조합 구하기
nCr = itertools.combinations(team, n // 2)
link = list(nCr)
# 가능한 팀조합개수
repeat = len(link)

# 팀별 차이값을 저장
result = []

# 조합의 개수만큼 반복
for i in link:
    # 스타트vs링크 팀 만들기, 점수 초기화
    start = team - set(i)
    start_score = 0
    link_score = 0
    res = 0
    # 스타트팀의 가능한 경우의 수
    for j in start:
        for k in start:
            start_score = start_score + array[j][k]
    # 링크팀의 가능한 경우의 수
    for p in i:
        for q in i:
            link_score = link_score + array[p][q]
    # 두팀의 점수차의 절댓값
    res = abs(start_score - link_score)
    result.append(res)

# 정답출력
print(min(result))