# 다단계 칫솔 판매
# https://school.programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    boss_ref = {}
    income_list = defaultdict(list)
    for idx, boss in enumerate(enroll):
        boss_ref[boss] = referral[idx]

    for idx, name in enumerate(seller):
        sell = name
        money = amount[idx] * 100
        while True:
            if boss_ref[sell] == "-":
                income_list[sell].append(money - int(money * 0.1))
                break
            else:
                income_list[sell].append(money - int(money * 0.1))
            sell = boss_ref[sell]
            money = int(money * 0.1)
            if money < 10:
                income_list[sell].append(money)
                break
    answer = []
    for i in enroll:
        answer.append(sum(income_list[i]))
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))