import math

# 링의 개수와 둘레비율
n = int(input())
array = list(map(int, input().split()))

# 기약분수로 나타내야 하므로 최대공약수 구해서 각각 나눔
for i in range(1, n):
    gcd = math.gcd(array[0], array[i])
    print(str(array[0]//gcd) + "/" + str(array[i]//gcd))