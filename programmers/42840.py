# https://programmers.co.kr/learn/courses/30/lessons/42840
# 모의고사
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score, answer = [0, 0, 0], []
    for index, value in enumerate(answers):
        if value == one[index % len(one)]:
            score[0] = score[0] + 1
        if value == two[index % len(two)]:
            score[1] = score[1] + 1
        if value == three[index % len(three)]:
            score[2] = score[2] + 1
    for index, value in enumerate(score):
        if value == max(score):
            answer.append(index + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))