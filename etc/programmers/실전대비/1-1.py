def solution(X, Y):
    intersection = []
    y = list(Y)
    for i in X:
        if i in y:
            intersection.append(i)
            y.remove(i)
    check = set(intersection)
    if len(intersection) == 0:
        return "-1"
    elif len(check) == 1 and "0" in check:
        return "0"
    else:
        return "".join(sorted(intersection, reverse=True))


def solution2(X, Y):
    result = []
    x, y = set(X), set(Y)
    x_num, y_num = [0] * 11, [0] * 11
    for i in X:
        x_num[int(i)] = x_num[int(i)] + 1
    for i in Y:
        y_num[int(i)] = y_num[int(i)] + 1

    intersection = x & y
    intersection = list(intersection)
    intersection.sort(reverse=True)

    for i in intersection:
        n = min(x_num[int(i)], y_num[int(i)])
        for _ in range(n):
            result.append(i)

    check = set(result)
    if len(result) == 0:
        return "-1"
    elif len(check) == 1 and "0" in check:
        return "0"
    else:
        return "".join(result)


print(solution2("100", "2345"))
print(solution2("100", "203045"))
print(solution2("100", "123450"))
print(solution2("12321", "42531"))
print(solution2("5525", "1255"))