# n보다 작은 한수 구하기 (n < 1000)
n = int(input())
# 세자리수 중에 한수
count = 0
# 한자리, 두자리수는 모두 한수
if n < 100:
    print(n)
# 3자리 수중 한수 구하기
else:
    for i in range(100, n + 1):
        i = str(i)
        first = int(i[0])
        second = int(i[1])
        third = int(i[2])
        if first - second == second - third:
            count = count + 1
    print(99 + count)