# 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            number = number + 1
        else:
            bin_num = bin(number)[2:]
            bin_num = "0" + bin_num
            one_idx = bin_num.rfind("0")
            bin_num = list(bin_num)
            bin_num[one_idx] = "1"
            bin_num[one_idx + 1] = "0"
            number = int("".join(bin_num), 2)
        numbers[index] = number
    return numbers


print(solution([2, 7]))
