# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))