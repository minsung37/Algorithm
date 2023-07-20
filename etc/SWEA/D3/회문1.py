# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi
# 1215. [S/W 문제해결 기본] 3일차 - 회문1
def count_palindrome(word):
    count = 0
    for i in range(size + 1 - n):
        check_word = word[i: i + n]
        if check_word == list(reversed(check_word)):
            count = count + 1
    return count


for t in range(10):
    size = 8
    n = int(input())
    graph = [list(input()) for _ in range(size)]
    result = 0
    for row in graph:
        result = result + count_palindrome(row)
    for x in range(size):
        col = []
        for y in range(size):
            col.append(graph[y][x])
        result = result + count_palindrome(col)
    print("#{} {}".format(t + 1, result))