# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도
def solution(k, dungeons):
    result = []
    visited = [False] * len(dungeons)

    def dfs(tired, count):
        for i in range(len(dungeons)):
            if tired >= dungeons[i][0]:
                if not visited[i]:
                    visited[i] = True
                    dfs(tired - dungeons[i][1], count + 1)
                    visited[i] = False
            else:
                result.append(count)
    dfs(k, 0)
    return max(result)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))