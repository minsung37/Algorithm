from collections import defaultdict


def dfs_find_root(v, array):
    if v == 1:
        return
    for i in tree_cp[v]:
        array.append(i)
        dfs_find_root(i, array)


def dfs(v):
    global size
    visited[v] = True
    size = size + 1
    for i in tree_pc[v]:
        if not visited[i]:
            dfs(i)


T = int(input())
for t in range(T):
    V, E, first, second = map(int, input().split())
    tree_cp = defaultdict(list)
    tree_pc = defaultdict(list)
    info = list(map(int, input().split()))
    first_list, second_list = [], []
    for i in range(0, 2 * E, 2):
        parent, child = info[i], info[i + 1]
        tree_cp[child].append(parent)
        tree_pc[parent].append(child)
    # 공통조상 찾기
    dfs_find_root(first, first_list)
    dfs_find_root(second, second_list)
    depth, root = 1000, 1
    for f_index, f_value in enumerate(first_list):
        for s_index, s_value in enumerate(second_list):
            if f_value == s_value:
                if f_index < depth:
                    root = f_value
                    depth = f_index
    # 공통조상부터 크기 구하기
    visited = [False] * (V + 1)
    size = 0
    dfs(root)
    print("#{} {} {}".format(t + 1, root, size))