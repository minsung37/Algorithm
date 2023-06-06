# 이모티콘 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/150368
def solution(users, emoticons):
    origin_discount = [10, 20, 30, 40]
    member, result = 0, []

    def backtracking(depth, discount):
        nonlocal member
        if depth == len(emoticons):
            total_member, total_cost = 0, 0
            for min_discount, cost in users:
                temp_cost = 0
                for index, rate in enumerate(discount):
                    if rate >= min_discount:
                        temp_cost = temp_cost + emoticons[index] * (100 - rate) // 100
                if temp_cost >= cost:
                    total_member = total_member + 1
                else:
                    total_cost = total_cost + temp_cost
            if member <= total_member:
                member = total_member
                result.append([member, total_cost])
            return

        for rate in origin_discount:
            discount.append(rate)
            backtracking(depth + 1, discount)
            discount.pop()

    backtracking(0, [])
    result.sort(key=lambda x: (x[0], x[1]))
    return result[-1]



print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))