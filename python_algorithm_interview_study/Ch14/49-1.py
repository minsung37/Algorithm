#
#
import collections


def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    if n <= 1:
        return [0]

    graph = collections.defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    leaves = []
    for i in range(n + 1):
        # 리프노드 추가
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을때까지 제거
    while n > 2:
        n = n - len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves