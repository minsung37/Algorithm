# 최대공약수와 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    return [gcd(n, m), lcm(n, m)]


print(solution(3, 12))
print(solution(2, 5))