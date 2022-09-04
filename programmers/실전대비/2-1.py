def solution(number):
    count = []
    n = len(number)
    for i in range(n):
        for j in range(n):
            if j != i:
                for k in range(n):
                    if k != i and k != j:
                        if number[i] + number[j] + number[k] == 0:
                            temp = [i, j, k]
                            temp.sort()
                            if temp not in count:
                                count.append(temp)
    return len(count)


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))