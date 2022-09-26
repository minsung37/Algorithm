# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from collections import defaultdict
from itertools import combinations
import operator

from collections import Counter


# 구린풀이
def solution(orders, course):
    result = []
    dic = defaultdict(int)
    dic2 = defaultdict(list)

    for i in course:
        for order in orders:
            for comb in combinations(sorted(order), i):
                dic[comb] = dic[comb] + 1
    sorted_by_value = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

    for idx, i in enumerate(sorted_by_value):
        if int(len(i[0])) not in dic2:
            dic2[len(i[0])].append(i[0])
            while True:
                if sorted_by_value[idx][1] == sorted_by_value[idx + 1][1] and len(sorted_by_value[idx][0]) == len(sorted_by_value[idx + 1][0]):
                    dic2[len(i[0])].append(sorted_by_value[idx + 1][0])
                else:
                    break
                idx = idx + 1
        if i[1] == 1:
            break

    for i in dic2:
        for j in dic2[i]:
            result.append("".join(j))

    return sorted(result)


# 효율적인 풀이
def solution2(orders, course):
    answer = []
    for i in course:
        order_list = []
        for order in orders:
            for comb in combinations(sorted(order), i):
                order_list.append("".join(comb))

        if order_list:
            order_list = Counter(order_list).most_common()
            max_count = order_list[0][1]

            for order in order_list:
                if order[1] == max_count and order[1] > 1:
                    answer.append(order[0])
                else:
                    break

        answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

print(solution2(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution2(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution2(["XYZ", "XWY", "WXA"], [2, 3, 4]))