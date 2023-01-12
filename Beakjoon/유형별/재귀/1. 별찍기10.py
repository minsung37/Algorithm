import sys
sys.setrecursionlimit(10**6)


def star(size):
    if size == 1:
        return ["*"]
    stars = star(size // 3)
    array = []
    # 상단부
    for i in stars:
        array.append(i * 3)
    # 중단부
    for i in stars:
        array.append(i + " " * (size // 3) + i)
    # 하단부
    for i in stars:
        array.append(i * 3)
    return array


n = int(input())
print('\n'.join(star(n)))