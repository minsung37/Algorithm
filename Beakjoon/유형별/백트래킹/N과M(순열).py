# 순열을 사용하기 위해
import itertools
# n, m 입력받기
n, m = map(int, input().split())
# 숫자리스트 만들기
array = []
for i in range(1, n + 1):
    array.append(i)
# 순열
nPr = itertools.permutations(array, m)
array2 = list(nPr)

# 순열로 만들수있는 경우의수 계산
array.sort(reverse=True)
repeat = 1
for i in range(m):
    repeat = repeat * array[i]
# print(len(array2)) 써도됨

# 출력
for i in range(repeat):
    for j in range(m):
        print(array2[i][j], end=" ")
    print("")
print(repeat)