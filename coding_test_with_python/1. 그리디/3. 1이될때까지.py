n, k = map(int, input().split())
count = 0

while True:
    if n % k == 0:
        n = n/k
    else:
        n = n - 1
    count = count + 1
    if n == 1:
        break

print(count)

# 1을 일일이 하나씩 빼므로 n이 커지면 효율적이지 못하다.