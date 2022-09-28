# 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    def convert(alpa):
        k = ord(alpa)
        if k >= 65 and k <= 90:
            k = k + n
            if k > 90:
                k = k - 26
            return chr(k)
        if k >= 97 and k <= 122:
            k = k + n
            if k > 122:
                k = k - 26
            return chr(k)

    result = ""
    for idx, i in enumerate(s):
        if i.isalpha():
            i = convert(i)
        result = result + i

    return result


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))