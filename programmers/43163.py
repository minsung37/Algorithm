# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환
from collections import deque


def solution(begin, target, words):
    def is_next(begin, target):
        count = 0
        for i in range(len(begin)):
            if begin[i] == target[i]:
                count = count + 1
        return count

    queue = deque()
    queue.append((begin, 0))
    y = 0
    if target not in words:
        return y
    while queue:
        x, y = queue.popleft()
        if x == target:
            return y
        for i in words:
            if is_next(x, i) == len(begin) - 1:
                queue.append((i, y + 1))
                words.remove(i)
    return y


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))