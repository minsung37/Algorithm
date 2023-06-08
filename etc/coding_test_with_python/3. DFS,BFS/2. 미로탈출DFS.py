n, m = map(int, input().split())
miro = []
res = 0
for i in range(n):
    miro.append(list(map(int, input())))


def move(x, y):
    global res
    # 벽을 벗어난경우 무시
    if x >= n or y >= m:
        return False
    # 최소 칸이므로 오른쪽, 아래로만 이동가능
    if miro[x][y] == 1:
        res = res + 1
        miro[x][y] = 0
        move(x + 1, y)
        move(x, y + 1)
    return res


print(move(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
