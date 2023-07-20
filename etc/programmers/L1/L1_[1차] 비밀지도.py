# [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    result = [[" "] * n for _ in range(n)]
    for index, pw in enumerate(arr1):
        pw = str(bin(pw)[2:])
        while len(pw) < n:
            pw = "0" + pw
        arr1[index] = pw

    for index, pw in enumerate(arr2):
        pw = str(bin(pw)[2:])
        while len(pw) < n:
            pw = "0" + pw
        arr2[index] = pw

    for x in range(n):
        for y in range(n):
            if arr1[x][y] == "1":
                result[x][y] = "#"
            if arr2[x][y] == "1":
                result[x][y] = "#"
    for index, temp in enumerate(result):
        result[index] = "".join(temp)
    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))