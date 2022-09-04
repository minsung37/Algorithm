from collections import defaultdict


def solution(n, lighthouse):
    maps = defaultdict(list)
    result = set()
    for x, y in lighthouse:
        maps[x].append(y)
        maps[y].append(x)
    for i in range(n):
        if maps[i + 1]:
            if len(maps[i + 1]) == 1:
                result.add(maps[i + 1][0])
    return len(result)


print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))