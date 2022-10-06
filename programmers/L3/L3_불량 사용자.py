# 불량 사용자
# https://school.programmers.co.kr/learn/courses/30/lessons/64064
def solution(user_id, banned_id):
    answer, result = [], [[]]
    for banned in banned_id:
        temp = []
        for user in user_id:
            if len(banned) == len(user):
                flag = True
                for idx, i in enumerate(user):
                    if banned[idx] != "*" and i != banned[idx]:
                        flag = False
                        break
                if flag:
                    for i in result:
                        if user not in i:
                            temp.append(i + [user])
        result = temp
    for i in result:
        if set(i) not in answer:
            answer.append(set(i))
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
