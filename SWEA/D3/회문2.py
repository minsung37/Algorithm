# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi
# 1216. [S/W 문제해결 기본] 3일차 - 회문2
def count_palindrome(word):
    result = 0
    for c in range(curr_len, size):
        for i in range(size + 1 - c):
            check_word = word[i: i + c]
            if check_word == list(reversed(check_word)):
                result = max(curr_len, c)
    return result


for t in range(10):
    size = 100
    curr_len = 0
    n = int(input())
    graph = [list(input()) for _ in range(size)]
    result = 0
    for row in graph:
        result = max(result, count_palindrome(row))
    for x in range(size):
        col = []
        for y in range(size):
            col.append(graph[y][x])
        result = max(result, count_palindrome(col))
    print("#{} {}".format(t + 1, result))
