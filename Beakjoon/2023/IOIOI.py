import sys
input = sys.stdin.readline

n, m, word = int(input()), int(input()), input().rstrip()
index, temp, result = 0, 0, 0

while index < m - 2:
    if word[index: index + 3] == "IOI":
        index = index + 2
        temp = temp + 1
        if temp == n:
            result = result + 1
            temp = temp - 1
    else:
        index = index + 1
        temp = 0
print(result)