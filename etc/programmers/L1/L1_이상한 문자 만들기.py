# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    result = ""
    count = 0
    for idx, i in enumerate(s):
        if i.isalpha():
            count = count + 1
            if count % 2 == 1:
                i = i.upper()
            else:
                i = i.lower()
        else:
            count = 0
        result = result + i
    return result


print(solution("try hello world"))