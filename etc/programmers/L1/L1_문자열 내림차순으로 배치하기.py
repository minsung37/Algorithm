# 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    return "".join(sorted(list(s), reverse=True))


print(solution("Zbcdefg"))
