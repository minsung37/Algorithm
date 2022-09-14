# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# [1차] 다트 게임
def solution(dartResult):
    dart = ""
    dart_info = dartResult + "."
    result = []

    if "10" in dart_info:
        dart_info = dart_info.replace("10", "a")

    def score(dart):

        if dart[0] == "a":
            score = 10
        else:
            score = int(dart[0])
        if "D" in dart:
            score = score ** 2
        if "T" in dart:
            score = score ** 3
        if "*" in dart:
            score = score * 2
            if len(result) != 0:
                result[-1] = result[-1] * 2
        if "#" in dart:
            score = -score
        result.append(score)

    for idx, i in enumerate(dart_info):
        if idx != 0:
            if i == "1" or i == "2" or i == "3" or i == "." \
                    or i == "4" or i == "5" or i == "6" or i == "7" \
                    or i == "8" or i == "9" or i == "a" or i == "0":
                score(dart)
                dart = ""
        dart = dart + i

    return sum(result)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))