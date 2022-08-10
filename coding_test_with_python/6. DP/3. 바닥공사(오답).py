# 정수 N을 입력받기
n = int(input())
d = [0] * (n + 1)
# d = [0,1,3,5]
d[0] = 0
d[1] = 1
d[2] = 3
d[3] = 5

for j in range(4,n + 1):
    for i in range(1, int(j//2) + 1):
        d[j] = d[j] + d[i] * d[j - i]

res = d[n] % 796796
print(res)
# 논리가 틀렸음!!