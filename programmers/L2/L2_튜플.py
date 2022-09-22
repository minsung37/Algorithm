# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    s = s[1:len(s) - 1]
    result, answer, temp, num = [], [], set(), ""

    for i in s:
        if i == "{":
            temp = set()
        elif i.isdigit():
            num = num + i
        elif i == "}":
            temp.add(num)
            result.append(list(temp))
        elif i == ",":
            temp.add(num)
            num = ""
    result.sort(key=len)

    for i in result:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))