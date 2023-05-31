def solution(data, col, row_begin, row_end):
    answer = 0
    # col 번째 값기준 오른차순 같으면 첫번째 기준 내림차순
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for index in range(row_begin - 1, row_end):
        temp = 0
        for value in data[index]:
            temp = temp + value % (index + 1)
        # XOR 연산
        answer = answer ^ temp
    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))
