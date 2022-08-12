# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기
def solution(n, wires):
    dif, result = n, 0
    for i in range(1, n - 1):
        left_, right_ = set(), set()
        left = wires[:i]
        right = wires[i:]
        for j in left:
            for k in j:
                left_.add(k)
        for j in right:
            for k in j:
                right_.add(k)
        if abs(len(left_) - len(right_)) < dif:
            result = i
            dif = abs(len(left_) - len(right_))
    return result - 1


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))