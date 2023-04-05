import sys
input = sys.stdin.readline


def backtraking(depth, password):
    if depth == n:
        result.append(password)
    for word in words:
        if len(password) == 0:
            backtraking(depth + 1, word)
        else:
            if ord(word) > ord(password[-1]):
                backtraking(depth + 1, password + word)


n, m = map(int, input().split())
words = list(input().split())
result = []
backtraking(0, "")
result.sort()
check = ['a', 'e', 'i', 'o', 'u']
for w in result:
    count = 0
    for i in w:
        if i in check:
            count = count + 1
    if count == 0:
        continue
    if len(w) - count < 2:
        continue
    print(w)