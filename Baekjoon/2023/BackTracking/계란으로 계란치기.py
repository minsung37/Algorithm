import sys
input = sys.stdin.readline


def backtraking(egg):
    global result
    if egg == n:
        count = 0
        for info in info_list:
            if info[0] <= 0:
                count = count + 1
        result = max(result, count)
        return
    # 손에든 계란 깨진경우
    if info_list[egg][0] <= 0:
        backtraking(egg + 1)
        return
    # 모두 깨진경우
    all_break = True
    for index, info in enumerate(info_list):
        if index == egg:
            continue
        if info[0] > 0:
            all_break = False
            break
    # 상황종료
    if all_break:
        result = max(result, n - 1)
        return
    for index, info in enumerate(info_list):
        # 자기 자신은 못침
        if index == egg:
            continue
        # 이미 깨진 경우
        if info[0] <= 0:
            continue
        info_list[egg][0] = info_list[egg][0] - info[1]
        info[0] = info[0] - info_list[egg][1]
        backtraking(egg + 1)
        info_list[egg][0] = info_list[egg][0] + info[1]
        info[0] = info[0] + info_list[egg][1]


n = int(input())
info_list = [list(map(int, input().split())) for _ in range(n)]
# 0 - 내구도, 1 - 무게
result = 0
backtraking(0)
print(result)