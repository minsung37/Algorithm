def solution(new_id):
    check = ["a", "b", "c", "d", "e",
             "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z",
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "-", "_", "."]
    second, third = "", ""
    # 1단계 - 소문자 치환
    new_id = new_id.lower()

    # 2단계 - 문자제거
    for i in new_id:
        if i in check:
            second = second + i

    # 3단계
    for i in second:
        if len(third) > 0:
            if not (third[-1] == "." and i == "."):
                third = third + i
        else:
            third = third + i

    # 4단계
    if len(third) > 0:
        if third[-1] == ".":
            third = third[0: -1]
        if len(third) > 1:
            if third[0] == ".":
                third = third[1:]

    # 5단계
    if len(third) == 0:
        third = "a"

    # 6단계
    if len(third) > 15:
        third = third[0:15]

    # 7단계
    if len(third) < 3:
        third = third + third[-1] + third[-1]
        third = third[0:3]
    if third[-1] == ".":
        third = third[0: 14]
    return third


print(solution("...!@BaT#*..y.abcdefghijklm."))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("m."))