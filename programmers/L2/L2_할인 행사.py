# 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount) - 9):
        temp = discount[i: i + 10]
        flag = True
        for j in dic:
            count = temp.count(j)
            if count < dic[j]:
                flag = False
                break
        if flag:
            answer = answer + 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))