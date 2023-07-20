# 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    for i in s:
        if i.isalpha():
            return False
    else:
        if len(s) == 4 or len(s) == 6:
            return True
        return False


print(solution("a234"))
print(solution("1234"))