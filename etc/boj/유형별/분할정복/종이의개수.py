import sys
input = sys.stdin.readline


def quad(x, y, n):
    # 전역변수 서정
    global paper,paper0,paper1,paper2
    # 첫번째 칸
    color = paper[x][y]
    flag = False
    for i in range(x, x + n):
        # 아래에서 재귀호출한경우 반복하지 않는다.
        if flag:
            break
        for j in range(y, y + n):
            # 첫번째칸과 일치 하지않는 경우 재귀호출
            if paper[i][j] != color:
                quad(x, y, n // 3)
                quad(x + (n // 3), y, n // 3)
                quad(x + 2 * (n // 3), y, n // 3)

                quad(x, y + n // 3, n // 3)
                quad(x + (n // 3), y + (n // 3), n // 3)
                quad(x + 2 * (n // 3), y + (n // 3), n // 3)

                quad(x, y + 2 * (n // 3), n // 3)
                quad(x + (n // 3), y + 2 * (n // 3), n // 3)
                quad(x + 2 * (n // 3), y + 2 * (n // 3), n // 3)

                flag = True
                break
    if not flag:
        if color == 0:
            paper0 = paper0 + 1
        elif color == 1:
            paper1 = paper1 + 1
        else:
            paper2 = paper2 + 1


# 문제조건 입력받기
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

paper0 = 0
paper1 = 0
paper2 = 0
quad(0, 0, n)

print(paper2)
print(paper0)
print(paper1)