# https://school.programmers.co.kr/learn/courses/30/lessons/81303
# 표 편집
# U X 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# D X 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# C 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다.
#   단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# Z 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
# 0 prev 1 value 2 next
def solution(n, k, cmd):

    stack = []
    chart = [[x - 1, x + 1, True] for x in range(n)]
    chart[0][0] = -1
    chart[-1][1] = -1

    for line in cmd:
        if line == "Z":
            num, prev, next = stack.pop()
            chart[num][2] = True
            if prev == -1:
                chart[next][0] = num
            elif next == -1:
                chart[prev][1] = num
            else:
                chart[next][0] = num
                chart[prev][1] = num
        elif line == "C":
            chart[k][2] = False
            prev, next = chart[k][0], chart[k][1]
            stack.append([k, prev, next])
            # 커서 이동
            if next == -1:
                k = chart[k][0]
            else:
                k = chart[k][1]
            # 연결관계
            if prev == -1:
                chart[next][0] = -1
            elif next == -1:
                chart[prev][1] = -1
            else:
                chart[prev][1] = next
                chart[next][0] = prev
        else:
            commend, offset = line.split(" ")
            offset = int(offset)
            if commend == "U":
                for _ in range(offset):
                    k = chart[k][0]
            if commend == "D":
                for _ in range(offset):
                    k = chart[k][1]
    result = []
    for i in range(n):
        if chart[i][2]:
            result.append("O")
        else:
            result.append("X")
    return "".join(result)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))