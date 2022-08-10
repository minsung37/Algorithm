n = int(input())


# 원판 개수, 시작, 중간, 옮길곳
def hanoi(n, start, mid, target):
    # 원판 한개인 경우
    if n == 1:
        print(start, target)
    else:
        # n - 1개의 원판을 중앙으로 이동
        hanoi(n - 1, start, target, mid)
        print(start, target)
        # n - 1개의 원판을 중앙에서 목표까지 이동
        hanoi(n - 1, mid, start, target)


print(2 ** n - 1)
hanoi(n, 1, 2, 3)