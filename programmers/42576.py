# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for index, name in enumerate(participant):
        if index == len(completion):
            return name
        if name != completion[index]:
            return name