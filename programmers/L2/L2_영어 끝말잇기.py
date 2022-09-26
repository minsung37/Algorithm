# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981
from collections import defaultdict


def solution(n, words):
    dic = defaultdict(list)
    result, last = [0, 0], ""

    for idx, word in enumerate(words):
        # 현재 까지나온 단어들
        now = words[:idx]
        # 중복말한경우
        if word in now:
            result[0], result[1] = idx % n + 1, len(dic[idx % n]) + 1
            break
        # 끝말(last)과 일치 하지 않는 경우
        if idx > 0:
            if last != word[0]:
                result[0], result[1] = idx % n + 1, len(dic[idx % n]) + 1
                break
        last = word[-1]
        dic[idx % n].append(word)
    return result


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

