# https://programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어
def solution(s):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result, stack = [], ""
    for i in s:
        try:
            i = int(i)
            if len(stack) != 0:
                result.append(str(number.index(stack)))
                stack = ""
            result.append(str(i))
        except:
            stack = stack + i
            if stack in number:
                result.append(str(number.index(stack)))
                stack = ""
    if stack:
        result.append(str(number.index(stack)))
    s = "".join(result)
    return int(s)