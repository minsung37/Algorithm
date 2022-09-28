# 3진법 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    def convert(k):
        rev_base = ''
        while k > 0:
            k, mod = divmod(k, 3)
            rev_base += str(mod)
        return rev_base[::-1]

    temp = convert(n)
    result = 0
    for idx, i in enumerate(temp):
        result = result + int(i) * (3 ** idx)
    return result


print(solution(45))
print(solution(125))