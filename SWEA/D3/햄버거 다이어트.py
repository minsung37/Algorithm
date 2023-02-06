def recursion(index, score, kcal):
    global result
    if kcal > l:
        return
    if score > result:
        result = score
    if index == n:
        return
    recursion(index + 1, score, kcal)
    recursion(index + 1, score + info[index][0], kcal + info[index][1])


t = int(input())
for i in range(t):
    n, l = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    recursion(0, 0, 0)
    print('#{} {}'.format(i + 1, result))