n = int(input())
b = 0

if n < 3:
    b = 1575 * (n + 1)
elif n == 3:
    b = 3600 + 1575 * 2
elif 3 < n < 13:
    b = 3600 + 1575 * n
elif n == 13:
    b = 3600 * 2 + 1575 * 12
elif 13 < n < 23:
    b = 3600 * 2 + 1575 * (n - 1)
elif n == 23:
    b = 3600 * 3 + 1575 * 21
print(b)
