def dfs(now, distance, count):
    global min_distance
    if min_distance < distance:
        return
    if count == n:
        distance = distance + cal(now, company)
        min_distance = min(distance, min_distance)
        return min_distance
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp = distance + cal(now, customers[i])
            dfs(customers[i], temp, count + 1)
            visited[i] = False


def cal(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


t = int(input())
for t in range(t):
    n = int(input())
    coordinate = list(map(int, input().split()))
    home, company = [coordinate[0], coordinate[1]], [coordinate[2], coordinate[3]]

    customers = []
    for i in range(4, len(coordinate), 2):
        customers.append([coordinate[i], coordinate[i + 1]])

    min_distance = int(1e9)
    visited = [False] * (len(customers))

    dfs(home, 0, 0)
    print("#" + str(t + 1), min_distance)