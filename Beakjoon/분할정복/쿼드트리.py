import sys
input = sys.stdin.readline


# 쿼드트리 함수 정의
def quad(x, y, n, z):
    # 사분면 파악
    location = z
    # 전역변수 설정
    global paper
    # 2사분면 일경우
    if location == 2:
        print("(", end="")
    color = paper[x][y]
    flag = False
    for i in range(x, x + n):
        # 아래에서 재귀호출한경우 반복하지 않는다.
        if flag:
            break
        for j in range(y, y + n):
            # 첫번째칸과 일치하지 않는경우 재귀호출
            if color != paper[i][j]:
                quad(x, y, n // 2, 2)  # 2사분면
                quad(x, y + n // 2, n // 2, 1)  # 1사분면
                quad(x + n // 2, y, n // 2, 3)  # 3사분면
                quad(x + n // 2, y + n // 2, n // 2, 4)  # 4사분면
                flag = True
                break
    # 재귀를 호출하지 않는경우 => 모든칸이 동일하다는뜻
    if not flag:
        if color == "1":
            print("1", end="")
        else:
            print("0", end="")
    # 4사분면 일경우
    if location == 4:
        print(")", end="")


# 문제조건 입력받기
n = int(input())
paper = []
for i in range(n):
    paper.append(input())

# 정답출력
quad(0, 0, n, 0)