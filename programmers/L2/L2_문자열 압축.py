# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축
def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        new_s, count = "", 1
        init = s[:i]
        for j in range(i, len(s) + 1245, i):
            compare = s[j:i + j]
            if init == compare:
                count = count + 1
            else:
                if count > 1:
                    new_s = new_s + str(count) + init
                else:
                    new_s = new_s + init
                init = compare
                count = 1
        result.append(len(new_s))
    return min(result)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))