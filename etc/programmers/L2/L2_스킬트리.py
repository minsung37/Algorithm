# 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    count = 0
    for x in skill_trees:
        temp = ""
        for i in x:
            if i in skill:
                temp = temp + i
        if temp == skill[:len(temp)]:
            count = count + 1
    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


