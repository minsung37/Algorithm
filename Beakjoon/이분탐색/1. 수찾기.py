# 리스트입력받기
n = int(input())
array = list(map(int, input().split()))
array.sort()

# 찾을값입력받기
comparison = int(input())
comparison_array = list(map(int, input().split()))


# 이진 탐색 매서드
def binary(a, t, s, e):
    while s <= e:
        m = (s + e) // 2
        if a[m] == t:
            return 1
        elif t < a[m]:
            e = m - 1
        elif t > a[m]:
            s = m + 1
    return None


# 탐색(탐색할곳, 탐색할값, start위치, 탐색할 곳의 end위치)
for i in comparison_array:
    if binary(array, i, 0, n - 1) is None:
        print(0)
    else:
        print(1)
