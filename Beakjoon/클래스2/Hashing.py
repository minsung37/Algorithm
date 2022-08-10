# 문자열과 길이 입력받기
n = int(input())
b = input()

# 해싱
result = 0
for i in range(n):
    a = ord(b[i]) - 96
    result = result + a * (31 ** i)

# mod
result = result % 1234567891

# 결과출력
print(result)