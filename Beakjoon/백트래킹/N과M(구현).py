# n : 리스트 m : 수열의길이
n, r = map(int, input().split())

# 숫자리스트 만들기
array = []
for i in range(1, n + 1):
    array.append(i)
array_r = sorted(array, reverse=True)

# 순열(nPr) 개수
nPr = []
num_nPr = 1
for i in range(r):
    num_nPr = num_nPr * array_r[i]
print("순열 :", num_nPr)
# for i in range(r):
#     for j in range(n):
#         if i != j:
#             nPr.append([array[i], array[j]])
# print(nPr)

# 조합(nCr) 개수
nCr = []
num_nCr = 1
for i in range(r):
    num_nCr = int(num_nCr * array_r[i] / array_r[n - 1 - i])
print("조합 :", num_nCr)

# 중복순열(nPir) 개수
nPir = []
num_nPir = n ** r
print("중복순열 :", num_nPir)

# 중복조합(cHr) 개수
nHr = []
num_nHr = 1
for i in range(r):
    num_nHr = int(num_nHr * (array_r[i] + r - 1) / array_r[n - 1 - i])
print("중복조합 :", num_nHr)
