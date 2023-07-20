# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 여행경로
from collections import defaultdict


def solution2(tickets):
    stack, result = ["ICN"], []
    tickets.sort(reverse=True)
    schedule = defaultdict(list)
    for now, next in tickets:
        schedule[now].append(next)

    while stack:
        start = stack.pop()
        if start in schedule and len(schedule[start]) > 0:
            stack.append(start)
            stack.append(schedule[start].pop())
        else:
            result.append(start)
    return result[::-1]


def solution(tickets):
    tickets, result = sorted(tickets, reverse=True), []
    schedule = defaultdict(list)
    for start, end in tickets:
        schedule[start].append(end)

    def dfs(next):
        # 다음 출발지가 있는경우
        while schedule[next]:
            dfs(schedule[next].pop())
        result.append(next)
    dfs('ICN')
    return result[::-1]


print(solution2([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution2([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution2([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))