# 후보키
# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from collections import defaultdict
from itertools import combinations


def solution(relation):
    # 유일키 아닌거 check에 담고, 유일키 개수 찾기
    check, dic = set(), defaultdict(list)
    n = len(relation[0])
    for infos in relation:
        for idx, info in enumerate(infos):
            if str(info) in dic[idx]:
                check.add(str(idx))
            dic[idx].append(info)
    result = n - len(check)

    # 유일키 제외하고 키 조합
    check, comb = sorted(list(check)), []
    for i in range(2, n + 1):
        temps = combinations(check, i)
        for temp in temps:
            temp = sorted(temp)
            comb.append("".join(temp))

    # 조합 중 후보키 찾기
    check_min = []
    for nums in comb:
        flag = True
        # 최소성 체크
        for i in check_min:
            if set(i).issubset(set(nums)):
                flag = False
                break
        if flag:
            checking = set()
            for j in range(len(relation)):
                temp = ""
                for num in nums:
                    temp = temp + dic[int(num)][j]
                checking.add(temp)
            if len(checking) == len(relation):
                check_min.append(nums)
                result = result + 1
            checking.clear()

    return result


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))

print(solution([["a", "1", "4"],
                ["2", "1", "5"],
                ["a", "2", "4"]]))
print(solution([["100", "r"],
                ["200", "c"],
                ["300", "d"]]))
print(solution([["1", "2", "3"],
                ["a", "b", "a"],
                ["c", "d", "c"],
                ["a", "f", "a"],
                ["b", "f", "b"]]))
