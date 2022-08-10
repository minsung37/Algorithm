import sys

# 리스트입력받기
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

# 찾을값입력받기
comparison = int(sys.stdin.readline())
comparison_array = list(map(int, sys.stdin.readline().split()))


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


# 값: 반복홧수 딕셔너리로 표현하기
count = {}
for i in array:
    try:
        count[i] = count[i] + 1
    except:
        count[i] = 1

# 탐색(탐색할곳, 탐색할값, start위치, 탐색할 곳의 end위치)
for i in comparison_array:
    res = 0
    if binary(array, i, 0, n - 1) is None:
        print(0, end=" ")
    else:
        # 각값이 몇개 있나 확인
        print(count[i], end=" ")