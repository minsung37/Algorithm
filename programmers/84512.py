# https://programmers.co.kr/learn/courses/30/lessons/84512
# 모음 사전
def solution(word):
    aeiou, words = ["A", "E", "I", "O", "U"], []

    def dfs(cnt, c):
        if cnt == 5:
            return
        for a in aeiou:
            temp = c + a
            words.append(temp)
            dfs(cnt + 1, temp)
    dfs(0, "")
    words.sort()
    return words.index(word) + 1


# 모음 사전 두번째 풀이
def solution2(word):
    alpa = ["A", "E", "I", "O", "U"]
    dic = []

    def dfs(word):
        if len(word) == 5:
            return
        for i in alpa:
            dic.append(word + i)
            dfs(word + i)
    dfs("")
    return dic.index(word) + 1