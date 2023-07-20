# 가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    count = []
    for i in range(len(s)):
        temp = s[:i + 1]
        for j in range(len(temp)):
            k = temp[j:]
            if k == k[::-1]:
                count.append(len(k))
    return max(count)


print(solution("abcdcba"))
print(solution("abacde"))