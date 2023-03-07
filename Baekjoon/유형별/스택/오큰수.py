# 수열의 정보입력받기
n = int(input())
array = list(map(int, input().split()))
stack = []

for i in range(n):
    # 스택이 차있는 경우
    while stack:
        # 스택에 있는 인덱스와 현재 비교대상을 비교
        # 현재가 더크다
        if array[i] > array[stack[-1]]:
            # 스택에 있는 인덱스를 가진 것을 현재 비교대상 값으로 바꿈
            array[stack.pop()] = array[i]
        # 아직 큰수가 안나왔으므로 인덱스를 스텍에 넣는다.
        else:
            stack.append(i)
            break
    # 스택이 비어있는 경우 0을 넣는다.
    if not stack:
        stack.append(i)

# 스텍에 있는 인덱스를 -1 로바꿈
# 오큰수를 찾지못한 경우
for i in stack:
    array[i] = -1

# *array => 배열에 있는것을 공백을 두고 출력한다.
print(*array)