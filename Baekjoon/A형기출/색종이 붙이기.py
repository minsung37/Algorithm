import sys
input = sys.stdin.readline


def backtracking(x, y, count):
    global result
    if y >= 10:
        result = min(result, count)
        return
    if x >= 10:
        backtracking(0, y + 1, count)
        return
    # 종이 붙여야함
    if paper[x][y] == 1:
        for size in range(1, 6):
            # 이미 5개 다붙인경우
            if paper_count[size] == 5:
                continue
            # 못붙이는 경우
            if x + size - 1 >= 10 or y + size - 1 >= 10:
                continue
            # 붙일 수 있나체크
            next_step = True
            for nx in range(x, x + size):
                for ny in range(y, y + size):
                    if paper[nx][ny] == 0:
                        next_step = False
                        break
                if not next_step:
                    break
            if next_step:
                for nx in range(x, x + size):
                    for ny in range(y, y + size):
                        paper[nx][ny] = 0
                paper_count[size] = paper_count[size] + 1
                backtracking(x + size, y, count + 1)
                paper_count[size] = paper_count[size] - 1
                for nx in range(x, x + size):
                    for ny in range(y, y + size):
                        paper[nx][ny] = 1
    else:
        backtracking(x + 1, y, count)


paper = [list(map(int, input().split())) for _ in range(10)]
result = int(1e9)
paper_count = [0, 0, 0, 0, 0, 0]
backtracking(0, 0, 0)
if result == int(1e9):
    print(-1)
else:
    print(result)