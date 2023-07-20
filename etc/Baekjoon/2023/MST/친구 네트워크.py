import sys
input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        # 합치면 친구수 더하기
        count[a] = count[a] + count[b]


t = int(input())
for _ in range(t):
    n = int(input())
    parent, count = {}, {}
    for _ in range(n):
        users = list(input().split())
        for user in users:
            # 새로운 유저면 부모 초기화
            if user not in parent:
                parent[user] = user
                count[user] = 1
        union(users[0], users[1])
        print(count[find(users[0])])
