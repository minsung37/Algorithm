# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    result = [1, 0]
    while True:
        if "0" in s:
            zero_count = s.count("0")
            s = "1" * (len(s) - zero_count)
            result[1] = result[1] + zero_count
        else:
            s = str(bin(len(s))[2:])
            result[0] = result[0] + 1
        if s == "1":
            break
    return result


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))