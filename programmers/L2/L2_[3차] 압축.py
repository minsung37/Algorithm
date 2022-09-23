# [3차] 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    # 사전 초기화
    answer = []
    dic, count, asc = dict(), 1, 65
    for i in range(26):
        dic[chr(asc)] = count
        count = count + 1
        asc = asc + 1

    # LZW
    left, right = 0, 1
    while right < len(msg) + 1:
        word = msg[left:right]
        if word in dic:
            right = right + 1
        else:
            answer.append(dic[word[:-1]])
            dic[word] = count
            count = count + 1
            left = right - 1
    answer.append(dic[word])
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))