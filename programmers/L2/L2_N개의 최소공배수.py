# N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    arr.sort()

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in arr:
        result = lcm(result, i)
    return result


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))