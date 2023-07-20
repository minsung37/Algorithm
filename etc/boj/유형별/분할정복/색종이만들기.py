import sys
input = sys.stdin.readline


# 쿼드트리 함수 정의
def quad(x, y, n):
    # 전역변수 설정
    global paper,white,blue
    # 첫번째칸
    color = paper[x][y]
    flag = False
    for i in range(x, x + n):
        # 아래에서 재귀호출한경우 반복하지 않는다.
        if flag:
            break
        for j in range(y, y + n):
            # 첫번째칸과 일치하지 않는경우 재귀호출
            if color != paper[i][j]:
                quad(x, y, n // 2)  # 2사분면
                quad(x, y + n // 2, n // 2)  # 1사분면
                quad(x + n // 2, y, n // 2)  # 3사분면
                quad(x + n // 2, y + n // 2, n // 2)  # 4사분면
                flag = True
                break
    # 재귀를 호출하지 않는경우 => 모든칸이 동일하다는뜻
    if not flag:
        if color == 1:
            blue = blue + 1
        else:
            white = white + 1


# 문제조건 입력받기
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0
quad(0, 0, n)
print(white)
print(blue)