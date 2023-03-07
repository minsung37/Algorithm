# 수 입력받기
n = int(input())

# 벌집이 1,7,19,37 이렇게 지나치는 방의 갯수가 같음
home = 1
room = 1

# 방 개수 찾기
while n > home:
    # 벌집이 6의 배수로 증가
    home = home + 6 * room
    # 반복문을 반복하는 횟수
    room = room + 1
print(room)
