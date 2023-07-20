# https://programmers.co.kr/learn/courses/30/lessons/42842
# 카펫
def solution(brown, yellow):
    # 직사각형 가능한 조합 구하기
    couple = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            couple.append([yellow // i, i])
    # brown 격자수 맞으면 크기 리턴
    for i in couple:
        if 2 * (sum(i) + 1 + 1) == brown:
            return [i[0] + 2, i[1] + 2]


print(solution(24, 24))