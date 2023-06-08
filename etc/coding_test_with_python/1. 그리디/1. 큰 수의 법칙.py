N, M, K = map(int, input().split())
n = list(map(int, input().split()))
n.sort(reverse=True)
s = 0
k = 0
# 연속 3(K)번까지 8번 더하기
for i in range(M):
    if k < K:
        s = s + n[0]
        k = k + 1
    else:
        k = 0
        s = s + n[1]

print(s)

# n이 커지면 시간초과, 변수명