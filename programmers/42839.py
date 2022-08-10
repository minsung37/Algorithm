# https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기
def solution(numbers):
    number = [str(i) for i in numbers]
    visited = [False] * len(number)
    num_list, temp, answer = [], [], []

    # 숫자 조합만들기
    def dfs(count):
        comb = temp[:]
        comb = ''.join(comb)
        if comb and int(comb) not in num_list:
            if int(comb) != 1 and int(comb) != 0:
                num_list.append(int(comb))
        if count == len(number):
            return
        for index, value in enumerate(number):
            if not visited[index]:
                temp.append(value)
                visited[index] = True
                dfs(count + 1)
                visited[index] = False
                temp.pop()

    # 소수 판별
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    dfs(0)
    for i in num_list:
        if check_prime(i):
            answer.append(i)
    return len(answer)


print(solution([0, 1, 1, 3]))