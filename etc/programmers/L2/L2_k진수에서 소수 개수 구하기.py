# k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def solution(n, k):
    # k진수로 변환
    def convert(num, k):
        k_num = ""
        while num > 0:
            num, mod = divmod(num, k)
            k_num = k_num + str(mod)
        return k_num[::-1]
    number = convert(n, k)

    # 소수 후보 리스트 만들기
    temp, prime_list = number.split("0"), []
    for i in temp:
        if len(i) > 0:
            prime_list.append(int(i))

    # 소수판별
    count = 0
    for prime in prime_list:
        if prime > 1:
            is_prime = True
            for i in range(2, int(prime ** 0.5) + 1):
                if prime % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count = count + 1
    return count


print(solution(437674, 3))
print(solution(110011, 10))