# 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    result, count = 0, len(name) - 1

    for index, alpha in enumerate(name):
        result = result + min(ord(alpha) - ord("A"), ord("Z") - ord(alpha) + 1)

        next = index + 1
        while next < len(name) and name[next] == "A":
            next = next + 1

        count = min((count, 2 * index + len(name) - next, index + 2 * (len(name) - next)))

    return result + count


print(solution("JEROEN"))
print(solution("JAAAAN"))
print(solution("J"))
print(solution("AAAA"))
print(solution("AN"))