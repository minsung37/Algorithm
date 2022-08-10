# 중복순열을 사용하기 위해
import itertools

# n, m 입력받기
n, m = map(int, input().split())

# 숫자리스트 만들기
array = []
for i in range(1, n + 1):
    array.append(i)

# 중복순열
nPir = itertools.product(array, repeat=m)
array2 = list(nPir)
repeat = len(array2)

# 출력
for i in range(repeat):
    for j in range(m):
        print(array2[i][j], end=" ")
    print("")
print(repeat)