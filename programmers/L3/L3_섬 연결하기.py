# 섬 연결하기
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    routes = set()
    routes.add(costs[0][0])

    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer = answer + cost[2]
                costs.pop(i)
                break
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
