# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산
from collections import defaultdict


def solution(fees, records):
    rate_list = defaultdict(int)
    time_list = defaultdict(list)
    answer = []

    # 시간계산하는 함수
    def time_convert(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    # 차량별 주차시간 구하기
    for record in records:
        time, num, enter = record.split()
        time_list[num].append(time)
    for car_num in time_list:
        if len(time_list[car_num]) % 2 == 1:
            time_list[car_num].append("23:59")
        for n in range(len(time_list[car_num]) // 2):
            start_time = time_convert(time_list[car_num][n * 2 + 1])
            endtime = time_convert(time_list[car_num][n * 2])
            rate_list[car_num] = rate_list[car_num] + (start_time - endtime)

    # 요금 계산
    for car_num in rate_list:
        if rate_list[car_num] <= fees[0]:
            rate_list[car_num] = fees[1]
        else:
            if (rate_list[car_num] - fees[0]) % fees[2] == 0:
                rate_list[car_num] = fees[1] + ((rate_list[car_num] - fees[0]) // fees[2]) * fees[3]
            else:
                rate_list[car_num] = fees[1] + (((rate_list[car_num] - fees[0]) // fees[2]) + 1) * fees[3]

    # 정답출력
    rate_list = sorted(rate_list.items())
    for i in rate_list:
        answer.append(i[1])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))