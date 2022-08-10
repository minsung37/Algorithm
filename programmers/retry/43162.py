# https://programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크
def solution(n, computers):
    answer, visited = 0, [False] * n

    def dfs(n, com):
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1 and not visited[connect]:
                dfs(n, connect)

    for com in range(n):
        if not visited[com]:
            dfs(n, com)
            answer = answer + 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
