import sys
from collections import deque

# 테스트케이스의 개수 입력받기
t = int(input())
for i in range(t):
    # 움직이는 방법(RRD)
    fuc = sys.stdin.readline().rstrip()
    # 수열의 크기
    m = int(input())
    # 수열 입력받기 [1,2,3,4]로 이루어짐
    array = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if m == 0:
        array = deque()
    flag = 0
    # 뒤집어 지는수
    r = 0
    for j in fuc:
        if j == "R":
            r = r + 1
        elif j == "D":
            if array:
                # 짝수이면 앞에서 뺀다
                if r % 2 == 0:
                    array.popleft()
                # 홀수면 뒤에서 뺀다
                else:
                    array.pop()
            # 큐가 빈경우
            else:
                print("error")
                flag = 1
                break
    # r이 홀수면 마지막에 뒤집어줘야함
    if flag == 0:
        if r % 2 == 0:
            print("[" + ",".join(array) + "]")
        else:
            array.reverse()
            print("[" + ",".join(array) + "]")