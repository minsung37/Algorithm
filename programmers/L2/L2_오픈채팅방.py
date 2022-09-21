# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    result, dic = [], {}

    for idx, item in enumerate(record):
        command = item.split()
        if command[0] == "Leave":
            result.append([command[1], "님이 나갔습니다."])
        else:
            dic[command[1]] = command[2]
            if command[0] == "Enter":
                result.append([command[1], "님이 들어왔습니다."])

    for idx, item in enumerate(result):
        result[idx] = dic[item[0]] + item[1]

    return result


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
