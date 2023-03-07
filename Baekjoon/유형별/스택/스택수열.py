# 수열크기입력받기
n = int(input())
stack = []
result = []
fail = 0
temp = 1
# 스택수열
for i in range(n):
    num = int(input())
    # pop할거 나올때까지 스택에 넣기
    while temp <= num:
        stack.append(temp)
        result.append("+")
        temp = temp + 1
    # pop 할거 나왔는데 그수와 같으면 pop하기
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    # pop 할거 나왔는데 그수와 같지 않다면 만들수가 없다.
    else:
        print("NO")
        fail = 1
        break
# 정답출력
if fail == 0:
    for i in result:
        print(i)